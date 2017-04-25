Tests that docstrings are handled properly at the app level.

  $ alias tap=$TESTDIR/002-app-docs.py


  $ tap -h
  usage: tap [-h]
  
  A simple test application to demonstrate how docstrings are used.
  
  optional arguments:
    -h, --help  show this help message and exit
  
  The first part of the docstring will be used as the ``description`` argument
  to the argument parser. If there is a blank line and then more text, as in
  this docstring, all the text following the blank line is used as the
  ``epilog``.
  [1]


  $ tap
