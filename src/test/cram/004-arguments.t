Tests exit code.

  $ alias tap=$TESTDIR/004-arguments.py


  $ tap -h
  usage: tap [-h] [-v]
  
  The first program with arguments!
  
  optional arguments:
    -h, --help     show this help message and exit
    -v, --verbose  output diagnostic information
  [1]


  $ tap


  $ tap -v
  you chose verbose


  $ tap --verbose
  you chose verbose
