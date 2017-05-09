# -*- coding: utf-8 -*-
"""


:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from __future__ import absolute_import, print_function
import argparse
import contextlib
import sys

from clik.compat import PY2, PY26, PY33


class HelpFormatter(argparse.HelpFormatter):
    def _format_usage(self, *args, **kwargs):
        parent = super(HelpFormatter, self)
        return parent._format_usage(*args, **kwargs)[:-1]


class ArgumentParserExit(Exception):
    def __init__(self, code):
        fmt = 'argument parser exited with return code %i'
        super(ArgumentParserExit, self).__init__(fmt % code)
        self.code = code


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        self._clik_bare_dests_recording = False
        self._clik_bare_dests = None
        kwargs.setdefault('formatter_class', HelpFormatter)
        super(ArgumentParser, self).__init__(*args, **kwargs)

    def exit(self, status=0, message=None):
        if message:
            print(message, end='', file=sys.stderr)
        raise ArgumentParserExit(status)

    @contextlib.contextmanager
    def _clik_bare_arguments(self):
        self._clik_bare_dests = []
        self._clik_bare_dests_recording = True
        yield
        self._clik_bare_dests_recording = False

    def add_argument(self, *args, **kwargs):
        # TODO: Disallow positional arguments if we are recording bare dests.
        argument = super(ArgumentParser, self).add_argument(*args, **kwargs)
        if self._clik_bare_dests_recording:
            self._clik_bare_dests.append(argument.dest)
        return argument

    def _format_usage(self, formatter):
        bare_dests = self._clik_bare_dests
        actions, bare_actions, subparsers = [], [], None
        for action in self._actions:
            if isinstance(action, argparse._SubParsersAction):
                subparsers = action
                actions.append(action)
            else:
                bare_actions.append(action)
                if bare_dests is None or action.dest not in bare_dests:
                    actions.append(action)
        prefix = 'usage: '
        mutex_groups = self._mutually_exclusive_groups
        if bare_dests is None or subparsers:
            formatter.add_usage(self.usage, actions, mutex_groups, prefix)
            prefix = '       '
        if bare_dests is not None:
            formatter.add_usage(self.usage, bare_actions, mutex_groups, prefix)
        return formatter

    def format_usage(self):
        return self._format_usage(self._get_formatter()).format_help()

    def format_help(self):
        formatter = self._get_formatter()
        self._format_usage(formatter)
        formatter.add_text('\n')
        formatter.add_text(self.description)
        for action_group in self._action_groups:
            formatter.start_section(action_group.title)
            formatter.add_text(action_group.description)
            formatter.add_arguments(action_group._group_actions)
            formatter.end_section()
        formatter.add_text(self.epilog)
        return formatter.format_help()


if PY33 or PY26:  # pragma: no cover (copypaste of Python 3.4 implementation)
    def __call__(self, parser, namespace, values, option_string=None):
        parser_name = values[0]
        arg_strings = values[1:]

        if self.dest is not argparse.SUPPRESS:
            setattr(namespace, self.dest, parser_name)

        try:
            parser = self._name_parser_map[parser_name]
        except KeyError:
            fmt = 'unknown parser %(parser_name)r (choices: %(choices)s)'
            args = {
                'parser_name': parser_name,
                'choices': ', '.join(self._name_parser_map),
            }
            raise argparse.ArgumentError(self, fmt % args)

        subnamespace, arg_strings = parser.parse_known_args(arg_strings, None)
        for key, value in vars(subnamespace).items():
            setattr(namespace, key, value)

        if arg_strings:
            vars(namespace).setdefault(argparse._UNRECOGNIZED_ARGS_ATTR, [])
            attr = getattr(namespace, argparse._UNRECOGNIZED_ARGS_ATTR)
            attr.extend(arg_strings)

    argparse._SubParsersAction.__call__ = __call__


if PY2:
    original_error = ArgumentParser.error

    def error(self, message=None):
        if message == 'too few arguments':
            for action in self._actions:  # pragma: no branch (unreachable)
                if isinstance(action, argparse._SubParsersAction):
                    break
            else:  # pragma: no cover (unreachable)
                raise Exception('this code should be unreachable')
            if action.required:
                self.print_usage(sys.stderr)
                fmt = '%s: error: the following arguments are required: %s\n'
                return self.exit(2, fmt % (self.prog, action.metavar))
        else:
            return original_error(self, message)

    ArgumentParser.error = error

    # https://gist.github.com/sampsyo/471779

    class _AliasedSubParsersPseudoAction(argparse.Action):
        def __init__(self, name, aliases, help):
            dest = name
            if aliases:
                dest += ' (%s)' % ', '.join(aliases)
            parent = super(_AliasedSubParsersPseudoAction, self)
            parent.__init__(option_strings=[], dest=dest, help=help)

    original_add_parser = argparse._SubParsersAction.add_parser

    def add_parser(self, name, **kwargs):
        aliases = kwargs.pop('aliases')
        parser = original_add_parser(self, name, **kwargs)
        for alias in aliases:
            self._name_parser_map[alias] = parser
        help = kwargs.pop('help')
        self._choices_actions.pop()
        action = _AliasedSubParsersPseudoAction(name, aliases, help)
        self._choices_actions.append(action)
        return parser

    argparse._SubParsersAction.add_parser = add_parser
