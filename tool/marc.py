# -*- coding: utf-8 -*-
"""
Marc is a backwards, underspecified, not-even-half-implemented cram.

The cram format is great, but after much fooling around with trying to get
cram working with coverage, I realized I could implement the tiny subset I
was using in a little tool that integrated coverage. So marc was born.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce and contributors, 2009-2018.
:license: BSD
"""
from __future__ import print_function
import difflib
import fnmatch
import os
import re
import shlex
import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class Test(object):
    """Test case."""

    def __init__(self, newlines, start_line, app, argv, invocation):
        """Initialize test case."""
        self.newlines = newlines
        self.start_line = start_line
        self.app = app
        self.argv = argv
        self.invocation = invocation
        self.expected_output = ''
        self.expected_exit_code = 0
        self.actual_output = None
        self.actual_exit_code = None

    def run(self):
        """Run test case."""
        exit_rvs = []

        def exit(rv):
            exit_rvs.append(rv)

        orig_stdout, orig_stderr = sys.stdout, sys.stderr
        out = sys.stdout = sys.stderr = StringIO()
        try:
            try:
                self.app.main(argv=['foo'] + self.argv, exit=exit)
            except Exception as e:
                out.write(u'Traceback (most recent call last):\n')
                out.write(u'  ...\n')
                out.write(u'%s: %s\n' % (e.__class__.__name__, e.args[0]))
                exit(1)
            if len(exit_rvs) != 1:
                fmt = 'Expected exactly 1 exit call, got %i (%s)'
                rvs = ', '.join(str(rv) for rv in exit_rvs)
                raise Exception(fmt % (len(exit_rvs), rvs))
            self.actual_exit_code = exit_rvs[0]
            self.actual_output = out.getvalue()
        finally:
            sys.stdout, sys.stderr = orig_stdout, orig_stderr


class TestFile(object):
    """Functional test case."""

    suffix = '.t'
    invocation_re = re.compile(r'^\$ dummy(?P<argv>.+)?$')
    exit_code_re = re.compile(r'^\[(?P<exit_code>\d+)\]$')
    app_name = 'dummy'

    @classmethod
    def discover(cls, path):
        """
        Auto-discover test files within ``path``.

        :param str path: Path to directory or file.
        :return: :class:`list` of :class:`TestFile` instances for each test
                 case in ``path``.
        """
        if os.path.isdir(path):
            rv = []
            for directory, _, filenames in os.walk(path):
                for filename in fnmatch.filter(filenames, '*%s' % cls.suffix):
                    rv.append(cls(os.path.join(directory, filename)))
            return rv
        elif os.path.isfile(path) and path.endswith(cls.suffix):
            return [cls(path)]

    def __init__(self, path):
        """
        Initialize functional test.

        :param str path: Base path to the test.
        """
        self.path = path
        self.script_path = '%s.py' % self.path[:-len(self.suffix)]
        self.name = path.rsplit('functional', 1)[1][1:-len(self.suffix)]
        self.failure = None
        self.result = '?'

    def run(self):
        """Run this test."""
        if os.path.exists(self.script_path):
            with open(self.script_path) as f:
                g = {}
                exec(f.read(), g)
                app = g[self.app_name]

            expected = ''
            tests = []
            with open(self.path) as f:
                test = None
                newlines = 0
                for i, line in enumerate(f):
                    expected += line
                    line = line.strip()
                    invocation_match = self.invocation_re.search(line)
                    exit_code_match = self.exit_code_re.search(line)
                    if invocation_match:
                        if test is not None:
                            fmt = 'error: missing exit value for test ' \
                                  'starting on line %i ("%s")'
                            fmt_args = (test.start_line, test.invocation)
                            self.failure = fmt % fmt_args
                            self.result = '!'
                            return
                        argv_raw = invocation_match.group('argv') or ''
                        argv = shlex.split(argv_raw)
                        test = Test(newlines, i + 1, app, argv, line)
                        newlines = 0
                    elif exit_code_match:
                        if test is None:
                            fmt = 'error: unexpected exit code on line %i'
                            self.failure = fmt % (i + 1)
                            self.result = '!'
                            return
                        exit_code = exit_code_match.group('exit_code')
                        test.expected_exit_code = exit_code
                        tests.append(test)
                        test = None
                    elif test:
                        test.expected_output += '%s\n' % line
                    else:
                        newlines += 1
            if test:
                fmt = 'error: missing exit value for test starting on line ' \
                      '%i ("%s")'
                self.failure = fmt % (test.start_line, test.invocation)
                self.result = '!'
                return

            actual = ''
            for test in tests:
                test.run()
                actual += '%s%s\n%s[%i]\n' % (
                    '\n' * test.newlines,
                    test.invocation,
                    test.actual_output,
                    test.actual_exit_code,
                )
            if actual == expected:
                self.result = '.'
                return
            diff = '\n'.join(list(difflib.unified_diff(
                expected.splitlines(),
                actual.splitlines(),
                n=1000,
                lineterm='',
            ))[3:])
            self.failure = '\n%s\n' % diff
            self.result = 'F'
        else:
            fmt = 'error: script file does not exist: %s'
            self.failure = fmt % self.script_path
            self.result = '!'


def main(argv=None, exit=sys.exit):
    """Entry point for the tool."""
    if argv is None:
        argv = sys.argv

    if len(sys.argv) < 2:
        msg = 'error: you must supply a test file or directory'
        print(msg, file=sys.stderr)
        exit(1)

    path = os.path.abspath(os.path.expanduser(os.path.expandvars(sys.argv[1])))
    test_files = TestFile.discover(path)
    if test_files is None:
        msg = 'error: test path does not exist: %s' % path
        print(msg, file=sys.stderr)
        exit(1)
    if len(test_files) < 1:
        print('error: no tests discovered for %s' % path, file=sys.stderr)
        exit(1)
    test_files = sorted(test_files, key=lambda tf: tf.name)

    for test_file in test_files:
        test_file.run()
        print(test_file.result, end='')
    print()

    successes, failures = 0, 0
    for test_file in test_files:
        if test_file.failure:
            print('\n\nFAILURE: %s\n%s' % (test_file.name, test_file.failure))
            failures += 1
        else:
            successes += 1

    fmt = 'ran %i tests (%i successes, %i failures)'
    print(fmt % (successes + failures, successes, failures))

    exit(1 if failures else 0)


if __name__ == '__main__':
    main()
