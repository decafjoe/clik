# -*- coding: utf-8 -*-
"""
Test the :mod:`clik.app` module.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce and contributors, 2009-2017.
:license: BSD
"""
import pytest

from clik.app import AttributeDict


def test_attribute_dict():
    """Test that :class:`clik.app.AtributeDict` behaves properly."""
    d = AttributeDict()
    assert d == {}
    d.foo = 'bar'
    assert d.foo == 'bar'
    assert d == {'foo': 'bar'}
    del d.foo
    assert d == {}
    with pytest.raises(KeyError):
        d.foo
    with pytest.raises(KeyError):
        del d.foo
