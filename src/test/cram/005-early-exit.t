Tests exiting after parser setup.

  $ alias tap=$TESTDIR/005-early-exit.py


  $ tap -h
  this will be printed...
  [42]


  $ tap
  this will be printed...
  [42]
