# -*- coding: utf-8 -*-
"""
Test the :mod:`clik.command` module.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce and contributors, 2009-2019.
:license: BSD
"""
import pytest

from clik import app
from clik.command import BareAlreadyRegisteredError


def test_docstring():
    """Test that the command instance gets the docstring of the function."""
    @app
    def dummy():
        """Test the docstring."""
        yield

    assert dummy.__doc__ == 'Test the docstring.'


def test_bare_already_registered_error():
    """Test that registering two bare commands raises an exception."""
    @app
    def dummy():
        yield

    @dummy.bare
    def dummy_bare():
        yield

    with pytest.raises(BareAlreadyRegisteredError):
        @dummy.bare
        def dummy_bare_2():
            yield
