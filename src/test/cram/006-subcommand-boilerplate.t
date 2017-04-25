Tests basic subcommand boilerplate.

  $ alias tap=$TESTDIR/006-subcommand-boilerplate.py


  $ tap -h
  usage: tap [-h] {clap,snap} ...
  
  Program with subcommands.
  
  optional arguments:
    -h, --help   show this help message and exit
  
  subcommands:
    {clap,snap}
      clap       Make the console clap (eventually).
      snap       Make the console snap (eventually).
  [1]


  $ tap
  usage: tap [-h] {clap,snap} ...
  tap: error: the following arguments are required: {clap,snap}
  [1]


  $ tap clap -h
  usage: tap clap [-h]
  
  Make the console clap (eventually).
  
  optional arguments:
    -h, --help  show this help message and exit
  [1]


  $ tap clap


  $ tap snap -h
  usage: tap snap [-h]
  
  Make the console snap (eventually).
  
  optional arguments:
    -h, --help  show this help message and exit
  [1]
  $ tap snap
