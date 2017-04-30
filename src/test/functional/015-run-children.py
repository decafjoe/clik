#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrates using "standard" exception-catching structure.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app, run_children


@app
def dummy():
    yield
    print('running setup code')
    try:
        run_children()
    except Exception as e:
        print('exception:', e)
    print('running tear down code')


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
    raise Exception('whoops')
