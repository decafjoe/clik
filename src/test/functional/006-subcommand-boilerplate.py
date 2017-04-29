#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests basic subcommand boilerplate.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik import app


@app
def tap():
    """Program with subcommands."""
    yield


@tap
def clap():
    """Make the console clap (eventually)."""
    yield


@tap
def snap():
    """Make the console snap (eventually)."""
    yield


if __name__ == '__main__':
    tap.main()
