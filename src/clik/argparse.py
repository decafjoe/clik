# -*- coding: utf-8 -*-
"""


:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
from __future__ import absolute_import, print_function
import argparse
import sys


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
        kwargs.setdefault('formatter_class', HelpFormatter)
        super(ArgumentParser, self).__init__(*args, **kwargs)

    def _clik_mark_command_arguments(self):
        self._clik_command_dests = []

    def add_argument(self, *args, **kwargs):
        argument = super(ArgumentParser, self).add_argument(*args, **kwargs)
        if hasattr(self, '_clik_command_dests'):
            self._clik_command_dests.append(argument.dest)
        return argument

    def exit(self, status=0, message=None):
        if message:
            print(message, end='', file=sys.stderr)
        raise ArgumentParserExit(status)

    def _format_usage(self, formatter):
        command_dests = getattr(self, '_clik_command_dests', ())
        global_actions, command_actions = [], []
        for action in self._actions:
            if not isinstance(action, argparse._SubParsersAction):
                command_actions.append(action)
            if action.dest not in command_dests:
                global_actions.append(action)
        mutex_groups = self._mutually_exclusive_groups
        formatter.add_usage(self.usage, global_actions, mutex_groups)
        if command_dests:
            formatter.add_usage(
                self.usage,
                command_actions,
                mutex_groups,
                '       ',
            )
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
