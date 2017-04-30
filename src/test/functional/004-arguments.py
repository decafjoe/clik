#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests basic argument handling.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app, args, parser


@app
def dummy():
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output diagnostic information',
    )

    yield

    if args.verbose:
        print('you chose verbose')
