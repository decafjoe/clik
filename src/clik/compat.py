# -*- coding: utf-8 -*-
"""


:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
import sys


PY2 = sys.version_info[0] == 2
PY26 = sys.version_info[0:2] == (2, 6)
PY33 = sys.version_info[0:2] == (3, 3)


if PY2:
    def iteritems(d, *args, **kwargs):
        return d.iteritems(*args, **kwargs)

    def implements_bool(cls):
        cls.__nonzero__ = cls.__bool__
        del cls.__bool__
        return cls
else:
    def iteritems(d, *args, **kwargs):
        return iter(d.items(*args, **kwargs))

    def implements_bool(cls):
        return cls
