# -*- coding: utf-8 -*-
"""
The command line interface kit.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from clik.app import app  # noqa: F401
from clik.command import catch  # noqa: F401
from clik.magic import args, current_app, g, parser, run_children  # noqa: F401
