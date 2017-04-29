#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrates using "standard" exception-catching structure.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app, args, parser


@app
def tap():
    """Program with subcommands."""
    yield
    print(args)
    print('running setup code')
    try:
        run_children()
    except Exception as e:
        print('exception:', e)
    print('running tear down code')


@tap.command
def tap_command():
    """Do this when no subcommand is given."""
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='this should only work on the command version',
    )
    yield
    print('hello')


@tap
def clap():
    """Make the console clap."""
    yield
    print('clap clap clap clap clap')


@tap
def snap():
    """Make the console snap."""
    yield
    print('snap snap snap snap snap')
    raise Exception('whoops')



if __name__ == '__main__':
    tap.main()
