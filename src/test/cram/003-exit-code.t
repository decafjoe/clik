Tests exit code.

  $ alias tap=$TESTDIR/003-exit-code.py


  $ tap -h
  usage: tap [-h]
  
  A program that always exits with an exit code of 42.
  
  optional arguments:
    -h, --help  show this help message and exit
  [1]


  $ tap
  [42]
