# -*- coding: utf-8 -*-
"""
All the hackery that makes clik clik.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
import re

from clik.magic import args, context

catch = object()


class Command(object):
    def __init__(self, fn, name=None, alias=None, aliases=None):
        self._fn = fn
        self._name = fn.__name__ if name is None else name
        self._aliases = [] if aliases is None else list(aliases)
        if alias:
            self._aliases.insert(0, alias)
        self._children = []
        self._command = None
        self._generator = None
        self._command_dests = []

    def __call__(self, fn=None, name=None, alias=None, aliases=None):
        def decorate(fn):
            command = Command(fn, name, alias, aliases)
            self._children.append(command)
            return command
        return decorate if fn is None else decorate(fn)

    def _split_docstring(_, x=None):
        parts = list(filter(None, re.split(r'\n\s*\n', x.__doc__ or '', 1)))
        return parts + [None] * (2 - len(parts))

    def _configure_parser(self, parser, cmd=None, rvs=None, cmd_dests=None):
        if cmd is None:
            cmd = []
        if rvs is None:
            rvs = []

        self._command_dests = cmd_dests or []

        self._generator = self._fn()
        with context(parser=parser):
            rvs.append(next(self._generator) or 0)

        cmd = cmd + [self]
        if self._children or self._command:
            metavar = ''
            if self._children:
                sorted_children = sorted(self._children, key=lambda x: x._name)
                metavar = '{%s}' % ','.join([c._name for c in sorted_children])
                if len(metavar) > parser._get_formatter()._width / 2.0:
                    metavar = '{command}'

            subparsers = parser.add_subparsers(
                dest='command',
                metavar=metavar,
                title='subcommands',
            )

            command_dests = None
            if self._command:
                parser._clik_mark_command_arguments()
                self._command._generator = self._command._fn()
                with context(parser=parser):
                    rvs.append(next(self._command._generator) or 0)
                command_dests = parser._clik_command_dests
                parser.set_defaults(_clik_cmd=cmd + [self._command])
            else:
                subparsers.required = True

            for child in self._children:
                description, epilog = self._split_docstring(child._fn)
                rvs.extend(child._configure_parser(
                    subparsers.add_parser(
                        child._name,
                        # TODO re-enable this
                        # This was commented out since it was causing
                        # problems on Python 2. Instead of solving
                        # the problem immediately, I want to see where
                        # else Python 2 breaks. Will deal with this
                        # eventually.
                        # aliases=child._aliases,
                        description=description,
                        epilog=epilog,
                        help=description,
                    ),
                    cmd=cmd,
                    rvs=rvs,
                    cmd_dests=command_dests,
                ))
        else:
            parser.set_defaults(_clik_cmd=cmd)

        return rvs

    def _run(self, rvs=None):
        if rvs is None:
            rvs = []

        command = args._clik_cmd.pop(0)

        for dest in self._command_dests:
            if hasattr(args, dest):
                delattr(args, dest)

        if len(args._clik_cmd) == 0:
            try:
                rv = next(command._generator)
            except StopIteration:
                rv = 0
        else:
            def run_children():
                return args._clik_cmd[0]._run(rvs)

            with context(run_children=run_children):
                try:
                    rv = next(command._generator)
                except StopIteration:
                    rv = 0

            if len(args._clik_cmd) > 0:
                send = None
                if rv is catch:
                    rv = 0
                    exception = None
                    try:
                        run_children()
                    except Exception as e:
                        exception = e
                    send = (rvs, exception)
                elif not rv:
                    run_children()
                    send = rvs
                if send:
                    try:
                        rv = command._generator.send(send)
                    except StopIteration:
                        rv = 0

        rvs.insert(0, rv)
        return rvs

    def command(self, fn):
        command = Command(fn)
        self._command = command
        return command
