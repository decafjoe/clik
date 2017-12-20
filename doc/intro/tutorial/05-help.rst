
.. _tutorial-05-help:

===================
 Tutorial 05: Help
===================

.. highlight:: python

Adding help text to the app is easy. Just add a docstring::

  @app
  def todo():
      """
      Command-line application for managing a todo list.

      The list is stored on disk as a simple JSON file containing an
      array of strings. The file path is controlled by the -f/--file
      argument (see documentation for that argument for more
      information).
      """
      yield
      print('Hello, world!')

.. highlight:: none

In argparse terms, the content before the first blank line is the
``description`` and all content after is the ``epilog``::

  $ ./todo -h
  usage: todo [-h]

  Command-line application for managing a todo list.

  optional arguments:
    -h, --help  show this help message and exit

  The list is stored on disk as a simple JSON file containing an array of
  strings. The file path is controlled by the -f/--file argument (see
  documentation for that argument for more information).

Easy peasy. Let's :ref:`implement the file argument
<tutorial-06-arguments>` described in the help text.
