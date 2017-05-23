
==================
 Functional Tests
==================

Or: the quickest possible introduction to clik. If you're an old hand
at Python and argparse, looking through the functional tests is
probably the best way to see what clik has to offer. I've tried to
order the tests to be expository, covering:

* the basics starting at 0000-boilerplate
* exit code handling starting at 0015-early-exit
* error handling starting at 0025-child-exit-code

The tests starting at 0100-early-exit-app are random various edge
cases that I thought of while building clik (or that came up as
untested in the coverage report). Don't worry about those.

The ``.py`` files are clik applications. The ``.t`` files show a
simulated terminal session.

Quick summaries of the expository tests are below.


Basics
======

* **0000-boilerplate** shows the minimum code needed to write a clik
  app
* **0001-app-docs** shows how to add help text to an application
* **0002-arguments** shows how to add and handle arguments
* **0003-subcommand-boilerplate** shows the boilerplate needed for
  "subcommand-style" applications
* **0004-subcommand-example** is a more fleshed out (and stupid and
  pointless) example of a subcommand-style application
* **0005-globals** introduces the global ``g`` object (a la Flask)
* **0006-cleanup** demonstrates how to write "cleanup" code that runs
  after the child command has been run
* **0007-aliases** shows how to define aliases for subcommands (also
  works on Python 2!)
* **0008-bare-command** -- you know how ``git remote`` can take
  subcommands (``add``, ``remove``, ``rename``, etc), but you can also
  just call ``git remote`` and it prints a list of remotes? Clik lets
  you do something like that. (And it, too, works on Python 2 as
  well!)


Exit Code
=========

* **0015-early-exit** shows how to exit during the parser
  configuration phase by ``yield`` -ing a non-zero exit code
* **0016-exit-code** shows how to set the exit code during the "run
  command" phase by ``yield`` -ing a non-zero exit code
* **0017-subcommand-exit-code** shows how to set the exit code from a
  subcommand
* **0018-subcommand-early-exit** shows that ``yield`` -ing non-zero
  from the parent returns that value immediately, without running the
  children
* **0019-subcommand-override** shows how parents can override the
  child exit code by ``yield`` -ing non-zero during the "cleanup" phase


Error Handling
==============

* **0025-child-exit-code** shows how to get the exit code of the child
* **0026-whoops-broken** shows exception handling code that you might
  intuitively think would work -- but it doesn't
* **0027-yield-catch** shows one way to capture exceptions from child
  code
* **0028-run-children** shows how to handle exceptions using the
  standard Python exception-handling constructs
