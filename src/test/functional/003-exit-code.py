#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests exit code.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def tap():
    """A program that always exits with an exit code of 42."""
    yield
    yield 42


if __name__ == '__main__':
    tap.main()
