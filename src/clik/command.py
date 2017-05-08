# -*- coding: utf-8 -*-
"""
All the hackery that makes clik clik.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from __future__ import print_function
import re
import sys

from clik.magic import args, context


catch = object()
STACK = '_clik_stack'
SHOW_SUBCOMMANDS = 3


class BareAlreadyRegisteredError(Exception):
    """Raised when a bare command function has already been registered."""

    def __init__(self, command):
        fmt = 'Bare command already registered for command "%s"'
        super(BareAlreadyRegisteredError, self).__init__(fmt % command._name)
        self.command = command


class Command(object):
    def __init__(self, fn, name=None, alias=None, aliases=None):
        self._bare = None
        self._children = []
        self._fn = fn
        self._generator = None
        self._parent = None
        self._parser = None

        if name is None:
            self._name = fn.__name__
        else:
            self._name = name

        if aliases is None:
            aliases = []
        else:
            aliases = list(aliases)
        if alias is not None:
            aliases.insert(0, alias)
        self._aliases = tuple(aliases)

    def bare(self, fn):
        if self._bare is not None:
            raise BareAlreadyRegisteredError(self)
        self._bare = Command(fn)
        return self._bare

    def __call__(self, fn=None, name=None, alias=None, aliases=None):
        def decorate(fn):
            self._children.append(Command(fn, name, alias, aliases))
            return self._children[-1]
        if fn is None:
            return decorate
        return decorate(fn)

    def _split_docstring(_, x=None):
        parts = list(filter(None, re.split(r'\n\s*\n', x.__doc__ or '', 1)))
        return parts + [None] * (2 - len(parts))

    def _configure_parser(self, parser, parent=None, stack=None):
        self._parser = parser

        if stack is None:
            stack = []
        if parent is not None:
            self._parent = parent

        self._generator = self._fn()
        with context(parser=parser):
            ec = next(self._generator)
            if ec:
                return ec

        stack = stack + [self]
        if self._bare:
            self._bare._generator = self._bare._fn()
            with parser._clik_bare_arguments():
                with context(parser=parser):
                    ec = next(self._bare._generator)
                    if ec:
                        return ec
            parser.set_defaults(**{STACK: stack + [self._bare]})

        if self._children:
            if len(self._children) > SHOW_SUBCOMMANDS:
                metavar = '{command}'
            else:
                names = ','.join([c._name for c in self._children])
                metavar = '{%s}' % names
            subparsers = parser.add_subparsers(
                dest='command',
                metavar=metavar,
                title='subcommands',
            )
            if not self._bare:
                subparsers.required = True
            for child in self._children:
                description, epilog = self._split_docstring(child._fn)
                subparser = subparsers.add_parser(
                    child._name,
                    aliases=child._aliases,
                    description=description,
                    epilog=epilog,
                    help=description,
                )
                ec = child._configure_parser(subparser, self, stack)
                if ec:
                    return ec

        if not self._bare and not self._children:
            parser.set_defaults(**{STACK: stack})

    def _check_bare_arguments(self):
        if self._parent is not None:
            parser = self._parent._parser
            if parser._clik_bare_dests is not None:
                for dest in parser._clik_bare_dests:
                    if getattr(args, dest) != parser.get_default(dest):
                        parser.print_usage(sys.stderr)
                        for action in parser._actions:  # pragma: no branch
                            if action.dest == dest:
                                break
                        else:  # pragma: no cover (unreachable)
                            raise Exception('this code should be unreachable')
                        options = '/'.join(action.option_strings)
                        err = 'unrecognized arguments when calling subcommand'
                        fmt = '%s: error: %s: %s'
                        msg = fmt % (parser.prog, err, options)
                        print(msg, file=sys.stderr)
                        return 1
                    delattr(args, dest)

    def _run(self, child=False):
        stack = getattr(args, STACK)

        if not child:
            for command in stack:
                ec = command._check_bare_arguments()
                if ec:
                    return ec

        command = stack.pop(0)

        if stack:
            def run_children():
                return stack[0]._run(child=True)

            with context(run_children=run_children):
                try:
                    ec = next(command._generator)
                except StopIteration:
                    ec = 0
            if ec and ec is not catch:
                return ec

            if stack:
                if ec is catch:
                    ec = 0
                    exception = None
                    try:
                        ec = run_children()
                    except Exception as e:
                        exception = e
                    send = (ec, exception)
                else:
                    send = ec = run_children()
                try:
                    ec = command._generator.send(send)
                except StopIteration:
                    pass
        else:
            try:
                ec = next(command._generator)
            except StopIteration:
                ec = 0

        return ec
