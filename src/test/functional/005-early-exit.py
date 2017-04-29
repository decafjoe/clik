#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests exiting after parser setup.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def tap():
    """Program showing early exit."""
    print('this will be printed...')
    yield 42
    print('...but this will not')


if __name__ == '__main__':
    tap.main()
