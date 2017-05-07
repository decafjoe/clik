# -*- coding: utf-8 -*-
"""
All the hackery that makes clik clik.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from __future__ import print_function
import argparse
import re
import sys

from clik.argparse import ArgumentParser, ArgumentParserExit
from clik.magic import args, context, current_app, g, parser, run_children


catch = object()


class AttributeDict(dict):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]


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
                description, epilog = split_docstring(child._fn)
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


class App(Command):
    def __init__(self, fn, name=None):
        name = fn.__name__ if name is None else name
        super(App, self).__init__(fn, name=name)

    def main(self, argv=None, exit=sys.exit):
        if argv is None:
            argv = sys.argv

        context.push('current_app', self)
        context.push('g', AttributeDict())
        context.push('args', None)  # Could do a argparse.Namespace here...

        description, epilog = split_docstring(self._fn)
        parser = ArgumentParser(
            prog=self._name,
            description=description,
            epilog=epilog,
        )
        nonzero_rvs = [rv for rv in self._configure_parser(parser) if rv != 0]
        if nonzero_rvs:
            return exit(nonzero_rvs[0])

        try:
            args = parser.parse_args(argv[1:])  # ...and pass it here...
        except ArgumentParserExit:
            return exit(1)

        context.pop('args')  # ...and kill this pop/push...
        context.push('args', args)

        # ...if we wanted to allow modification of the global `args`
        # during parser configuration. I like that commands can't
        # mutate args until we know they're being called. But I could
        # probably be convinced to change that.

        nonzero_rvs = [rv for rv in self._run() if rv != 0]
        if nonzero_rvs:
            return exit(nonzero_rvs[0])
        return exit(0)


def split_docstring(cls):
    parts = list(filter(None, re.split(r'\n\s*\n', cls.__doc__ or '', 1)))
    return parts + [None] * (2 - len(parts))


def app(fn=None, name=None):
    def decorate(fn):
        return App(fn, name)
    return decorate if fn is None else decorate(fn)
