#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Access the exception via the yield.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app, catch


@app
def tap():
    """Program with subcommands."""
    yield
    print('running setup code')
    child_exit_codes, exception = (yield catch)
    print('exception:', exception)
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
    raise Exception('whoops')



if __name__ == '__main__':
    tap.main()
