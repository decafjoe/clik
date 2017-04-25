Access the exception via the yield.

  $ alias tap=$TESTDIR/015-run-children.py


  $ tap clap
  running setup code
  clap clap clap clap clap
  running tear down code


  $ tap snap
  running setup code
  snap snap snap snap snap
  exception: whoops
  running tear down code
