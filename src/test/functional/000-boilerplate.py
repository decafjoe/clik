#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The most trivial possible app.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def dummy():
    yield
