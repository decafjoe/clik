#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrates exiting early, before child commands get invoked.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app, args, parser


@app
def tap():
    """Program with subcommands."""
    parser.add_argument(
        '-f',
        '--fail',
        action='store_true',
        default=False,
        help='fail without invoking the child command',
    )

    yield

    if args.fail:
        yield 42


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



if __name__ == '__main__':
    tap.main()
