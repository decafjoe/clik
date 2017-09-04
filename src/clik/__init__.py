# -*- coding: utf-8 -*-
"""
The command line interface kit.

Clik is a tool for writing complex command-line interfaces with minimal
boilerplate and bookkeeping.

This top-level package pulls together the end user API from the various
modules within clik.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce and contributors, 2009-2017.
:license: BSD
"""
__version__ = '0.90.0'


from clik.app import app, args, current_app, g, parser, run_children  # noqa
from clik.command import catch  # noqa: F401
