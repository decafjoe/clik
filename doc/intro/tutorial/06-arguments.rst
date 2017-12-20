
.. _tutorial-06-arguments:

========================
 Tutorial 06: Arguments
========================

clik provides two "magic" variables for configuring and accessing
arguments: the aptly-named ``parser`` and ``args``::

  from clik import app, args, parser

  @app
  def todo():
      # ... snip ...
      parser.add_argument(
          '-f',
          '--file',
          default='todo.json',
          help='file in which to store data (default: %(default)s)',
      )
      yield
      print('File path is:', args.file)

``parser`` is an :class:`argparse.ArgumentParser`. ``args`` is an
:class:`argparse.Namespace` – the same thing you would get back from
:meth:`argparse.ArgumentParser.parse_args`.

This might remind you of the "execution phases" from step 4, which
should make more sense now::

  def todo():
      # configure argument parser
      yield  # give control back to clik, which parses end user arguments
      # do something with parsed arguments

.. highlight:: none

The behavior of the application is what you probably expect::

  $ ./todo -h
  usage: todo [-h] [-f FILE]

  Command-line application for managing a todo list.

  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  file in which to store data (default: todo.json)

  The list is stored on disk as a simple JSON file containing an array of
  strings. The file path is controlled by the -f/--file argument (see
  documentation for that argument for more information).

  $ ./todo
  File is: todo.json

  $ ./todo -f myfile.json
  File is: myfile.json

  $ ./todo -f=myfile.json
  File is: myfile.json

  $ ./todo -fmyfile.json
  File is: myfile.json

  $ ./todo --file myfile.json
  File is: myfile.json

  $ ./todo --file=myfile.json
  File is: myfile.json

.. highlight:: python

Of course, the code before the ``yield`` is not limited to simple
calls to ``add_argument``. It's just arbitrary Python code. As a silly
example::

  from datetime import datetime
  from clik import app, args, parser

  @app
  def todo():
      # If it's 6PM or later, default to the "nighttime list,"
      # otherwise default to the "daytime list."
      if datetime.today().time().hour > 17:
          default = 'night.json'
      else:
          default = 'day.json'
      parser.add_argument(
          '-f',
          '--file',
          default=default,
          help='file in which to store data (default: %(default)s)',
      )
      yield
      print('File path is:', args.file)

As is often the case, with great power comes great responsibility.
Code before the ``yield`` is run on every invocation of the program…

* …regardless of whether the arguments are valid or not
* …even if ``-h/--help`` is specified
* …or, in the case of subcommands, even if the subcommand is not
  called!

In other words: **don't do expensive things before the yield** or your
program will feel/be unresponsive. (The Python interpreter startup
time is bad enough.)

To finish this step, let's make the argument "do" something::

  #!bin/python
  # -*- coding: utf-8; mode: python -*-
  import json
  import os

  from clik import app, args, parser


  @app
  def todo():
      """
      Command-line application for managing a todo list.
  
      The list is stored on disk as a simple JSON file containing an
      array of strings. The file path is controlled by the -f/--file
      argument (see documentation for that argument for more
      information).
      """
      parser.add_argument(
          '-f',
          '--file',
          default='todo.json',
          help='file in which to store data (default: %(default)s)',
      )

      yield

      item_list = []
      if os.path.exists(args.file):
          with open(args.file) as f:
              item_list = json.load(f)

      for item in item_list:
          print('*', item)


  if __name__ == '__main__':
      todo.main()

.. highlight:: json

Assuming a ``test.json`` file with the following contents…

::

  [
    "Pick up nails from hardware store",
    "Grab milk from the grocery",
    "Clean up the kitchen",
    "Feed the cats"
  ]

.. highlight:: none

…the application can now print out the items in the todo list::

  $ ./todo
  $ ./todo -f test.json
  * Pick up nails from hardware store
  * Grab milk from the grocery
  * Clean up the kitchen
  * Feed the cats
  $

Next we'll get into the thick of what makes clik useful, and start
implementing the interface we designed way back in step 0! :ref:`Get
ready for subcommands! <tutorial-07-subcommands>`
