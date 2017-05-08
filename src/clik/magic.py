# -*- coding: utf-8 -*-
"""


:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
import contextlib
import copy

from clik.compat import implements_bool, iteritems, PY2


class MagicNameConflictError(Exception):
    def __init__(self, name):
        msg = 'The magic variable name "%s" is already registered' % name
        super(MagicNameConflictError, self).__init__(msg)
        self.name = name


class UnregisteredMagicNameError(Exception):
    def __init__(self, name):
        msg = 'The magic variable "%s" is not registered' % name
        super(UnregisteredMagicNameError, self).__init__(msg)
        self.name = name


class UnboundMagicError(Exception):
    def __init__(self, name):
        msg = 'The magic variable "%s" is not bound' % name
        super(UnboundMagicError, self).__init__(msg)
        self.name = name


class Context(object):
    def __init__(self):
        self._registry = []
        self._state = {}

    @contextlib.contextmanager
    def __call__(self, **kwargs):
        keys = []
        for key, value in iteritems(kwargs):
            self.push(key, value)
            keys.append(key)
        yield
        for key in keys:
            self.pop(key)

    def get(self, name):
        if name not in self._registry:
            raise UnregisteredMagicNameError(name)
        if not self._state[name]:
            raise UnboundMagicError(name)
        return self._state[name][0]

    def push(self, name, object):
        if name not in self._registry:
            raise UnregisteredMagicNameError(name)
        self._state[name].insert(0, object)

    def pop(self, name):
        if name not in self._registry:
            raise UnregisteredMagicNameError(name)
        if not self._state[name]:
            raise UnboundMagicError(name)
        return self._state[name].pop(0)

    def register(self, name):
        if name in self._registry:
            raise MagicNameConflictError(name)
        self._registry.append(name)
        self._state[name] = []


context = Context()


@implements_bool
class Magic(object):  # pragma: no cover (werkzeug implementation)
    def __init__(self, name, context=context):
        context.register(name)
        object.__setattr__(self, '_Magic__name', name)
        object.__setattr__(self, '_Magic__context', context)

    def _get_current_object(self):
        """Return the current object."""
        return self.__context.get(self.__name)

    @property
    def __dict__(self):
        try:
            return self._get_current_object().__dict__
        except RuntimeError:
            raise AttributeError('__dict__')

    def __repr__(self):
        try:
            obj = self._get_current_object()
        except RuntimeError:
            return '<%s unbound>' % self.__class__.__name__
        return repr(obj)

    def __bool__(self):
        try:
            return bool(self._get_current_object())
        except RuntimeError:
            return False

    def __unicode__(self):
        try:
            return unicode(self._get_current_object())  # noqa
        except RuntimeError:
            return repr(self)

    def __dir__(self):
        try:
            return dir(self._get_current_object())
        except RuntimeError:
            return []

    def __getattr__(self, name):
        if name == '__members__':
            return dir(self._get_current_object())
        return getattr(self._get_current_object(), name)

    def __setitem__(self, key, value):
        self._get_current_object()[key] = value

    def __delitem__(self, key):
        del self._get_current_object()[key]

    if PY2:
        __getslice__ = lambda x, i, j: x._get_current_object()[i:j]

        def __setslice__(self, i, j, seq):
            self._get_current_object()[i:j] = seq

        def __delslice__(self, i, j):
            del self._get_current_object()[i:j]

    def __setattr__(x, n, v): return setattr(x._get_current_object(), n, v)
    def __delattr__(x, n): return delattr(x._get_current_object(), n)
    def __str__(x): return str(x._get_current_object())
    def __lt__(x, o): return x._get_current_object() < o
    def __le__(x, o): return x._get_current_object() <= o
    def __eq__(x, o): return x._get_current_object() == o
    def __ne__(x, o): return x._get_current_object() != o
    def __gt__(x, o): return x._get_current_object() > o
    def __ge__(x, o): return x._get_current_object() >= o
    def __cmp__(x, o): return cmp(x._get_current_object(), o)
    def __hash__(x): return hash(x._get_current_object())
    def __call__(x, *a, **kw): return x._get_current_object()(*a, **kw)
    def __len__(x): return len(x._get_current_object())
    def __getitem__(x, i): return x._get_current_object()[i]
    def __iter__(x): return iter(x._get_current_object())
    def __contains__(x, i): return i in x._get_current_object()
    def __add__(x, o): return x._get_current_object() + o
    def __sub__(x, o): return x._get_current_object() - o
    def __mul__(x, o): return x._get_current_object() * o
    def __floordiv__(x, o): return x._get_current_object() // o
    def __mod__(x, o): return x._get_current_object() % o
    def __divmod__(x, o): return x._get_current_object().__divmod__(o)
    def __pow__(x, o): return x._get_current_object() ** o
    def __lshift__(x, o): return x._get_current_object() << o
    def __rshift__(x, o): return x._get_current_object() >> o
    def __and__(x, o): return x._get_current_object() & o
    def __xor__(x, o): return x._get_current_object() ^ o
    def __or__(x, o): return x._get_current_object() | o
    def __div__(x, o): return x._get_current_object().__div__(o)
    def __truediv__(x, o): return x._get_current_object().__truediv__(o)
    def __neg__(x): return -(x._get_current_object())
    def __pos__(x): return +(x._get_current_object())
    def __abs__(x): return abs(x._get_current_object())
    def __invert__(x): return ~(x._get_current_object())
    def __complex__(x): return complex(x._get_current_object())
    def __int__(x): return int(x._get_current_object())
    def __long__(x): return long(x._get_current_object())
    def __float__(x): return float(x._get_current_object())
    def __oct__(x): return oct(x._get_current_object())
    def __hex__(x): return hex(x._get_current_object())
    def __index__(x): return x._get_current_object().__index__()
    def __coerce__(x, o): return x._get_current_object().__coerce__(x, o)
    def __enter__(x): return x._get_current_object().__enter__()
    def __exit__(x, *a, **kw):
        return x._get_current_object().__exit__(*a, **kw)
    def __radd__(x, o): return o + x._get_current_object()
    def __rsub__(x, o): return o - x._get_current_object()
    def __rmul__(x, o): return o * x._get_current_object()
    def __rdiv__(x, o): return o / x._get_current_object()
    if PY2:
        def __rtruediv__(x, o): return x._get_current_object().__rtruediv__(o)
    else:
        __rtruediv__ = __rdiv__
    def __rfloordiv__(x, o): return o // x._get_current_object()
    def __rmod__(x, o): return o % x._get_current_object()
    def __rdivmod__(x, o): return x._get_current_object().__rdivmod__(o)
    def __copy__(x): return copy.copy(x._get_current_object())
    def __deepcopy__(x, memo):
        return copy.deepcopy(x._get_current_object(), memo)


current_app = Magic('current_app')
parser = Magic('parser')
args = Magic('args')
g = Magic('g')
run_children = Magic('run_children')
