# -*- coding: utf-8 -*-
"""
All the hackery that makes clik clik.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
import sys

from clik.argparse import ArgumentParser, ArgumentParserExit
from clik.command import Command
from clik.magic import context


def app(fn=None, name=None):
    def decorate(fn):
        return App(fn, name)
    if fn is None:
        return decorate
    return decorate(fn)


class AttributeDict(dict):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]


class App(Command):
    def __init__(self, fn, name=None):
        super(App, self).__init__(fn, name=name)

    def main(self, argv=None, exit=sys.exit):
        if argv is None:
            argv = sys.argv

        context.push('current_app', self)
        context.push('g', AttributeDict())
        context.push('args', None)  # Could do a argparse.Namespace here...

        description, epilog = self._split_docstring(self._fn)
        parser = ArgumentParser(
            prog=self.name,
            description=description,
            epilog=epilog,
        )
        nonzero_ecs = [ec for ec in self._configure_parser(parser) if ec != 0]
        if nonzero_ecs:
            return exit(nonzero_ecs[0])

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

        nonzero_ecs = [ec for ec in self._run() if ec != 0]
        if nonzero_ecs:
            return exit(nonzero_ecs[0])
        return exit(0)
