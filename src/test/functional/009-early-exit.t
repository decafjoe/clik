Demonstrates exiting early, before child commands get invoked.

  $ alias tap=$TESTDIR/009-early-exit.py


  $ tap -h
  usage: tap [-h] [-f] {clap,snap} ...
  
  Program with subcommands.
  
  optional arguments:
    -h, --help   show this help message and exit
    -f, --fail   fail without invoking the child command
  
  subcommands:
    {clap,snap}
      clap       Make the console clap.
      snap       Make the console snap.
  [1]


  $ tap clap
  clap clap clap clap clap


  $ tap -f clap
  [42]
