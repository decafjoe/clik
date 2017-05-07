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
STACK = '_clik_stack'
SHOW_SUBCOMMANDS = 3


class BareAlreadyRegisteredError(Exception):
    """Raised when a bare command function has already been registered."""

    def __init__(self, command):
        msg = 'Bare command already registered for command "%s"' % command.name
        super(BareAlreadyRegisteredError, self).__init__(msg)
        self.command = command


class Command(object):
    def __init__(self, fn, name=None, alias=None, aliases=None):
        self._bare = None
        self._bare_dests = []
        self._children = []
        self._fn = fn
        self._generator = None
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

    @property
    def aliases(self):
        return self._aliases

    @property
    def name(self):
        return self._name

    def bare(self, fn):
        if self._bare is not None:
            raise BareAlreadyRegisteredError(self)
        self._bare = fn

    def __call__(self, fn=None, name=None, alias=None, aliases=None):
        def decorate(fn):
            command = Command(fn, name, alias, aliases)
            self._children.append(command)
            return command
        if fn is None:
            return decorate
        return decorate(fn)

    def _split_docstring(_, x=None):
        parts = list(filter(None, re.split(r'\n\s*\n', x.__doc__ or '', 1)))
        return parts + [None] * (2 - len(parts))

    def _configure_parser(self, parser, stack=None, ecs=None, bare_dests=None):
        self._parser = parser

        if stack is None:
            stack = []
        if ecs is None:
            ecs = []

        if bare_dests is None:
            self._bare_dests = ()
        else:
            self._bare_dests = bare_dests

        self._generator = self._fn()
        with context(parser=parser):
            ec = next(self._generator)
            if ec is None:
                ec = 0
            # TODO: validate return code? (integer -- what range?)
            #       throw exception if invalid?
            ecs.append(ec)

        stack = stack + [self]
        if self._children or self._bare:
            metavar = ''
            if self._children:
                sorted_children = sorted(self._children, key=lambda x: x._name)
                if len(sorted_children) > SHOW_SUBCOMMANDS:
                    metavar = '{command}'
                else:
                    names = ','.join([c._name for c in sorted_children])
                    metavar = '{%s}' % names

            subparsers = parser.add_subparsers(
                dest='command',
                metavar=metavar,
                title='subcommands',
            )

            bare_dests = None
            if self._bare:
                parser._clik_mark_bare_arguments_start()
                self._bare._generator = self._bare._fn()
                with context(parser=parser):
                    ec = next(self._command._generator)
                    if ec is None:
                        ec = 0
                    ecs.append(ec)
                bare_dests = tuple(parser._clik_bare_dests)
                parser.set_defaults(**{STACK: stack + [self._bare]})
            else:
                subparsers.required = True

            for child in self._children:
                description, epilog = self._split_docstring(child._fn)
                ecs.extend(child._configure_parser(
                    subparsers.add_parser(
                        child.name,
                        aliases=child.aliases,
                        description=description,
                        epilog=epilog,
                        help=description,
                    ),
                    stack=stack,
                    ecs=ecs,
                    bare_dests=bare_dests,
                ))
        else:
            parser.set_defaults(**{STACK: stack})

        return ecs

    def _run(self, ecs=None):
        if ecs is None:
            ecs = []

        stack = getattr(args, STACK)
        command = stack.pop(0)

        for dest in self._bare_dests:
            if hasattr(args, dest):
                if getattr(args, dest) != self._parser.get_default(dest):
                    # TODO error out: unrecognized argument: ...
                    #      (i.e. imitate argparse as best as possible)
                    ecs.append(1)
                    return ecs
                delattr(args, dest)

        if len(stack) == 0:
            try:
                ec = next(command._generator)
            except StopIteration:
                ec = 0
        else:
            def run_children():
                return stack[0]._run(ecs)

            with context(run_children=run_children):
                try:
                    ec = next(command._generator)
                except StopIteration:
                    ec = 0

            if len(stack) > 0:
                send = None
                if ec is catch:
                    ec = 0
                    exception = None
                    try:
                        run_children()
                    except Exception as e:
                        exception = e
                    send = (ecs, exception)
                elif not ec:
                    run_children()
                    send = ecs
                if send:
                    try:
                        ec = command._generator.send(send)
                    except StopIteration:
                        ec = 0

        ecs.insert(0, ec)
        return ecs