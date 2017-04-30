#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrates the g object.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app, args, g, parser


@app
def dummy():
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output more stuff',
    )

    yield

    g.number = 10 if args.verbose else 5


@dummy
def foo():
    parser.add_argument(
        '-l',
        '--loud',
        action='store_true',
        default=False,
        help='foo louder',
    )

    yield

    msg = 'FOO' if args.loud is True else 'foo'
    print(' '.join([msg for _ in range(g.number)]))


@dummy
def bar():
    parser.add_argument(
        '-f',
        '--fast',
        action='store_true',
        default=False,
        help='bar faster',
    )

    yield

    join_character = '' if args.fast is True else ' '
    print(join_character.join(['bar' for _ in range(g.number)]))
