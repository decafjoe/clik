#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Shows how to access exit codes from child commands.

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
    # Since commands can be nested arbitrarily deep (more info on that
    # later), there may be more than one child. So this is a list of
    # integers instead of a single integer.
    child_exit_codes = (yield)
    print('child exit codes:', child_exit_codes)
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
