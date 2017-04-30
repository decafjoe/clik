#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests basic subcommand boilerplate.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def dummy():
    """Program with subcommands."""
    yield


@dummy
def foo():
    """Foo all the things."""
    yield


@dummy
def bar():
    """Bar all over the place."""
    yield
