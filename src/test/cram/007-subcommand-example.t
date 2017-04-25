Basic example to demonstrate subcommands.

  $ alias tap=$TESTDIR/007-subcommand-example.py


  $ tap -h
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  usage: tap [-h] [-v] {clap,snap} ...
  
  Program with subcommands.
  
  optional arguments:
    -h, --help     show this help message and exit
    -v, --verbose  output more stuff
  
  subcommands:
    {clap,snap}
      clap         Make the console clap.
      snap         Make the console snap.
  
  Note that in real programs, you probably won't be printing stuff to the
  console in the "configure parser" block of code. It's in this example only to
  show control flow.
  [1]


  $ tap clap -h
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  usage: tap clap [-h] [-l]
  
  Make the console clap.
  
  optional arguments:
    -h, --help  show this help message and exit
    -l, --loud  clap louder
  [1]


  $ tap snap -h
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  usage: tap snap [-h] [-f]
  
  Make the console snap.
  
  optional arguments:
    -h, --help  show this help message and exit
    -f, --fast  snap faster
  [1]


For some reason cram seems to always put stderr before stdout. In reality,
the lines starting with "configuring" are output first, and the usage/error
messages after that:

  $ tap
  usage: tap [-h] [-v] {clap,snap} ...
  tap: error: the following arguments are required: {clap,snap}
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  [1]


  $ tap clap
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  invoking the code after the yield in "tap"
  invoking clap
  clap clap clap clap clap


  $ tap --verbose clap
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  invoking the code after the yield in "tap"
  invoking clap
  clap clap clap clap clap clap clap clap clap clap


  $ tap clap --loud
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  invoking the code after the yield in "tap"
  invoking clap
  CLAP CLAP CLAP CLAP CLAP


  $ tap --verbose clap --loud
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  invoking the code after the yield in "tap"
  invoking clap
  CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP CLAP


See note above about stdout/stderr being swapped:

  $ tap clap --verbose
  usage: tap [-h] [-v] {clap,snap} ...
  tap: error: unrecognized arguments: --verbose
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  [1]


  $ tap snap
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  invoking the code after the yield in "tap"
  invoking snap
  snap snap snap snap snap
  [42]


  $ tap --verbose snap
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  invoking the code after the yield in "tap"
  invoking snap
  snap snap snap snap snap snap snap snap snap snap
  [42]


  $ tap snap --fast
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  invoking the code after the yield in "tap"
  invoking snap
  snapsnapsnapsnapsnap
  [42]


  $ tap --verbose snap --fast
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  invoking the code after the yield in "tap"
  invoking snap
  snapsnapsnapsnapsnapsnapsnapsnapsnapsnap
  [42]


See note above about stdout/stderr being swapped:

  $ tap snap --verbose
  usage: tap [-h] [-v] {clap,snap} ...
  tap: error: unrecognized arguments: --verbose
  configuring top-level parser
  configuring clap parser
  configuring snap parser
  [1]
