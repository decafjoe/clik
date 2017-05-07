$ dummy -h
usage: dummy [-h] [-v] {bar,foo} ...
       dummy [-h] [-v] [-t]

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose
  -t, --test

subcommands:
  {bar,foo}
    foo
    bar
[1]


$ dummy
in dummy, args.verbose: False
in dummy_bare, args.verbose: False
in dummy_bare, args.test: False
[0]


$ dummy -vt
in dummy, args.verbose: True
in dummy_bare, args.verbose: True
in dummy_bare, args.test: True
[0]


$ dummy foo -h
usage: dummy foo [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy foo
in dummy, args.verbose: False
in foo, args.verbose: False
[0]


$ dummy -v foo
in dummy, args.verbose: True
in foo, args.verbose: True
[0]


$ dummy -t foo
usage: dummy [-h] [-v] {bar,foo} ...
       dummy [-h] [-v] [-t]
dummy: error: unrecognized arguments when calling subcommand: -t/--test
[1]


$ dummy bar -h
usage: dummy bar [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar
in dummy, args.verbose: False
in bar, args.verbose: False
Traceback (most recent call last):
  ...
AttributeError: 'Namespace' object has no attribute 'test'
[1]
