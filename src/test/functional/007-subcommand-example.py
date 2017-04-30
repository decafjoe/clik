#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic example to demonstrate subcommands.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app, args, parser


@app
def dummy():
    print('configuring top-level parser')
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output more stuff',
    )

    yield

    print('invoking the code after the yield in "dummy"')


@dummy
def foo():
    print('configuring foo parser')
    parser.add_argument(
        '-l',
        '--loud',
        action='store_true',
        default=False,
        help='foo louder',
    )

    yield

    print('invoking foo')
    msg = 'FOO' if args.loud else 'foo'
    number = 10 if args.verbose else 5
    print(' '.join([msg for _ in range(number)]))


@dummy
def bar():
    print('configuring bar parser')
    parser.add_argument(
        '-f',
        '--fast',
        action='store_true',
        default=False,
        help='bar faster',
    )

    yield

    print('invoking bar')
    join_character = '' if args.fast else ' '
    number = 10 if args.verbose else 5
    print(join_character.join(['bar' for _ in range(number)]))

    yield 42
