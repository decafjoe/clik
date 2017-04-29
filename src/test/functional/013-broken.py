#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Adds child exceptions to the mix.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def tap():
    """
    Program with subcommands.

    Note that this program does not work correctly!
    """
    yield
    print('running setup code')
    try:
        yield
    except Exception as e:
        print('running tear down code')
        print(e)


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
