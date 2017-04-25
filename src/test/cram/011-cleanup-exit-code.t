Demonstrates setting exit code after running tear down.

  $ alias tap=$TESTDIR/011-cleanup-exit-code.py


  $ tap clap
  running setup code
  clap clap clap clap clap
  running tear down code
  [7]


  $ tap snap
  running setup code
  snap snap snap snap snap
  running tear down code
  [7]
