Demonstrates the "tear down" block for parent commands.

  $ alias tap=$TESTDIR/010-cleanup.py


  $ tap clap
  running setup code
  clap clap clap clap clap
  running tear down code


  $ tap snap
  running setup code
  snap snap snap snap snap
  running tear down code
  [42]
