#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests that docstrings are handled correctly at the app level.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def tap():
    """
    A simple test application to demonstrate how docstrings are used.

    The first part of the docstring will be used as the ``description``
    argument to the argument parser. If there is a blank line and then more
    text, as in this docstring, all the text following the blank line is
    used as the ``epilog``.
    """
    yield


if __name__ == '__main__':
    tap.main()
