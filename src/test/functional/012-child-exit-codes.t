Shows how to access exit codes from child commands.

  $ alias tap=$TESTDIR/012-child-exit-codes.py


  $ tap clap
  running setup code
  clap clap clap clap clap
  child exit codes: [0]
  running tear down code


  $ tap snap
  running setup code
  snap snap snap snap snap
  child exit codes: [42]
  running tear down code
  [42]
