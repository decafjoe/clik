#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Adds child exceptions to the mix.

Note: this program is broken!

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def dummy():
    yield
    print('running setup code')
    try:
        yield
    except Exception as e:
        print('running tear down code')
        print(e)


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
    raise Exception('whoops')
