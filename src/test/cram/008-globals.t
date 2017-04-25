Demonstrates the g object.

  $ alias tap=$TESTDIR/008-globals.py


  $ tap clap
  clap clap clap clap clap


  $ tap --verbose clap
  clap clap clap clap clap clap clap clap clap clap


  $ tap snap
  snap snap snap snap snap
  [42]


  $ tap --verbose snap
  snap snap snap snap snap snap snap snap snap snap
  [42]
