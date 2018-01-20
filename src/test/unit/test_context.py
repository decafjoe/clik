# -*- coding: utf-8 -*-
"""
Test the :mod:`clik.context` module.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce and contributors, 2009-2018.
:license: BSD
"""
import pytest

from clik.context import Context, LockedMagicError, MagicNameConflictError, \
    UnboundMagicError, UnregisteredMagicNameError
from clik.magic import Magic


def test_context():
    """Test all the behavior and corner cases of contexts."""
    context = Context()
    a = Magic('a')
    with context.acquire(a):
        with pytest.raises(LockedMagicError):
            with context.acquire(a):
                pass
        with pytest.raises(MagicNameConflictError):
            context.register('a')
        with pytest.raises(UnboundMagicError):
            assert a
        with pytest.raises(UnboundMagicError):
            context.pop('a')
        with pytest.raises(UnregisteredMagicNameError):
            context.get('z')
        with pytest.raises(UnregisteredMagicNameError):
            context.push('z', None)
        with pytest.raises(UnregisteredMagicNameError):
            context.pop('z')
        with context(a=5):
            assert a == 5
            with context(a=10):
                assert a == 10
            assert a == 5
        with pytest.raises(UnboundMagicError):
            assert a
