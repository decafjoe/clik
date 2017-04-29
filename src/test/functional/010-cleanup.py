#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrates the "tear down" block for parent commands.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def tap():
    """Program with subcommands."""
    yield
    print('running setup code')
    yield
    print('running tear down code')


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
    yield 42



if __name__ == '__main__':
    tap.main()
