# -*- coding: utf-8 -*-
"""


:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce and contributors, 2009-2017.
:license: BSD
"""
import contextlib

from clik.compat import iteritems


class LockedMagicError(Exception):
    def __init__(self, name):
        msg = 'The magic variable "%s" is currently locked' % name
        super(LockedMagicError, self).__init__(msg)
        self.name = name


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

    @contextlib.contextmanager
    def acquire(self, *magic_variables):
        for variable in magic_variables:
            if variable._Magic__context is not None:
                raise LockedMagicError(variable._Magic__context)
            self.register(variable._Magic__name)
            object.__setattr__(variable, '_Magic__context', self)
        try:
            yield
        finally:
            for variable in magic_variables:
                self.unregister(variable._Magic__name)
                object.__setattr__(variable, '_Magic__context', None)

    def _assert_in_registry(self, name):
        if name not in self._registry:
            raise UnregisteredMagicNameError(name)

    def get(self, name):
        self._assert_in_registry(name)
        if not self._state[name]:
            raise UnboundMagicError(name)
        return self._state[name][0]

    def push(self, name, object):
        self._assert_in_registry(name)
        self._state[name].insert(0, object)

    def pop(self, name):
        self._assert_in_registry(name)
        if not self._state[name]:
            raise UnboundMagicError(name)
        return self._state[name].pop(0)

    def register(self, name):
        if name in self._registry:
            raise MagicNameConflictError(name)
        self._registry.append(name)
        self._state[name] = []

    def unregister(self, name):
        self._assert_in_registry(name)
        self._registry.remove(name)
        del self._state[name]
