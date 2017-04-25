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
def tap():
    """
    Program with subcommands.

    Note that in real programs, you probably won't be printing stuff to the
    console in the "configure parser" block of code. It's in this example
    only to show control flow.
    """
    print('configuring top-level parser')
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output more stuff',
    )

    yield

    print('invoking the code after the yield in "tap"')


@tap
def clap():
    """Make the console clap."""
    print('configuring clap parser')
    parser.add_argument(
        '-l',
        '--loud',
        action='store_true',
        default=False,
        help='clap louder',
    )

    yield

    print('invoking clap')
    msg = 'CLAP' if args.loud else 'clap'
    number = 10 if args.verbose else 5
    print(' '.join([msg for _ in range(number)]))


@tap
def snap():
    """Make the console snap."""
    print('configuring snap parser')
    parser.add_argument(
        '-f',
        '--fast',
        action='store_true',
        default=False,
        help='snap faster',
    )

    yield

    print('invoking snap')
    join_character = '' if args.fast else ' '
    number = 10 if args.verbose else 5
    print(join_character.join(['snap' for _ in range(number)]))

    # This will be the exit code when snap is invoked.
    yield 42


if __name__ == '__main__':
    tap.main()
