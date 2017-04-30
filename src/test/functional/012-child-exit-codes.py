#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Shows how to access exit codes from child commands.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def dummy():
    yield
    print('running setup code')
    child_exit_codes = (yield)
    print('child exit codes:', child_exit_codes)
    print('running tear down code')


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
    yield 42
