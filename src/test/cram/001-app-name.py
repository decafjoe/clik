#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests that the app name can specified.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app(name='tappity')
def tap():
    yield


if __name__ == '__main__':
    tap.main()
