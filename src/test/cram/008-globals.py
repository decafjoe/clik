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
def tap():
    """Program with subcommands."""
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output more stuff',
    )

    yield

    g.number = 10 if args.verbose else 5


@tap
def clap():
    """Make the console clap."""
    parser.add_argument(
        '-l',
        '--loud',
        action='store_true',
        default=False,
        help='clap louder',
    )

    yield

    msg = 'CLAP' if args.loud is True else 'clap'
    print(' '.join([msg for _ in range(g.number)]))


@tap
def snap():
    parser.add_argument(
        '-f',
        '--fast',
        action='store_true',
        default=False,
        help='snap faster',
    )

    yield

    join_character = '' if args.fast is True else ' '
    print(join_character.join(['snap' for _ in range(g.number)]))

    # This will be the exit code when snap is invoked.
    yield 42


if __name__ == '__main__':
    tap.main()
