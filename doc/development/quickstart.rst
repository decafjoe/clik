
============
 Quickstart
============


Prerequisites
=============

Requirements:

* Common development tools like git, make, a C compiler, etc
* Python 3.6 -- this is the "main" interpreter used for development
* Virtualenv

Recommendations:

* All supported Python interpreters

  * Python 2.6
  * Python 2.7
  * Python 3.3
  * Python 3.4
  * Python 3.5
  * Python 3.6
  * PyPy
  * PyPy 3

Suggestions:

* LaTeX -- for building the documentation as a PDF


Setup
=====

The repository can be cloned anywhere you like on your local machine.
At any time, you can delete the entire project and its environment by
``rm -rf`` -ing the local directory.

.. highlight:: bash

The following instructions clone the repository to ``~/clik``::

   cd
   git clone https://github.com/decafjoe/clik.git
   cd clik
   make env

Wait ~10m and you should be good to go!

Note that all dependencies are installed underneath the repository
directory (take a peek at ``.env/``). To delete the development
environment artifacts, you can run ``make pristine`` (see below). To
delete everything, simply ``rm -rf`` the clone.


Tooling
=======

Clik's developer tooling is exposed via ``make``. Run ``make`` with no
arguments to get a list of available targets. All targets except
``make release`` are idempotent, so they can be run at any time.

Environment:

* ``make env`` installs the development environment; subsequent runs
  update the environment if required
* ``make clean`` deletes build artifacts like .pyc files, sdists, etc
* ``make pristine`` kills the local development environment
* ``make check-update`` checks for updates to Python packages
  installed in the development environment

Documentation:

* ``make html`` generates the HTML documentation to
  ``doc/_build/html/``
* ``make pdf`` generates the PDF documentation to
  ``doc/_build/latex/clik.pdf``
* ``make docs`` builds both HTML and PDF documentation to their
  respective locations

Build:

* ``make dist`` builds a sdist into ``dist/``
* ``make release`` builds a clean sdist, uploads it to PyPI, tags the
  commit with the current version number, bumps the version, then
  commits the new version number and pushes it up to GitHub (this is
  largely implemented by the ``tool/pre-release`` and
  ``tool/post-release`` scripts)

QA:

* ``make lint`` runs the Flake8 linter on the Python files in the
  project
* ``make test`` runs the functional and unit test suites against the
  "main" development interpreter
* ``make test-all`` runs the linter, runs the functional and unit test
  suites against all supported interpreters, and generates a coverage
  report to ``coverage/``

Be aware of ``tool/test``. It allows for precise selection of what
tests to run. It's a time-saver when working on a small part of the
codebase. Instead of running the entire test suite after every change,
you can simply run the relevant tests. See ``tool/test -h`` for more
information.
