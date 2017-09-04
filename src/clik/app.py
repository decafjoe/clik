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
from clik.context import Context
from clik.magic import Magic


args = Magic('args')
current_app = Magic('current_app')
g = Magic('g')
parser = Magic('parser')
run_children = Magic('run_children')


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
        super(App, self).__init__(Context(), fn, name=name)

    def main(self, argv=None, exit=sys.exit):
        if argv is None:  # pragma: no cover (hard to test, obviously correct)
            argv = sys.argv

        description, epilog = self._split_docstring(self._fn)
        root_parser = ArgumentParser(
            prog=self._name,
            description=description,
            epilog=epilog,
        )

        with self._ctx.acquire(args, current_app, g, parser, run_children):
            with self._ctx(current_app=self, g=AttributeDict()):
                with self._ctx(args=None):
                    ec = self._configure_parser(root_parser)
                if ec:
                    return exit(ec)
                try:
                    with self._ctx(args=root_parser.parse_args(argv[1:])):
                        return exit(self._run())
                except ArgumentParserExit:
                    return exit(1)
