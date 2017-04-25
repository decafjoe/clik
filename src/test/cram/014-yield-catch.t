Access the exception via the yield.

  $ alias tap=$TESTDIR/014-yield-catch.py


  $ tap clap
  running setup code
  clap clap clap clap clap
  exception: None
  running tear down code


  $ tap snap
  running setup code
  snap snap snap snap snap
  exception: whoops
  running tear down code
