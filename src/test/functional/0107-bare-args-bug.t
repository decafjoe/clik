$ dummy -h
usage: dummy [-h] {foo,bar} ...
       dummy [-h] [-t TEST]

optional arguments:
  -h, --help            show this help message and exit
  -t TEST, --test TEST

subcommands:
  {foo,bar}
    foo
    bar
[1]


$ dummy
in dummy
in dummy_bare, args.test: wibble
[0]


$ dummy -t wobble
in dummy
in dummy_bare, args.test: wobble
[0]


$ dummy foo -h
usage: dummy foo [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy foo
in dummy
in foo
[0]


$ dummy -t wobble foo
usage: dummy [-h] {foo,bar} ...
       dummy [-h] [-t TEST]
dummy: error: unrecognized arguments when calling subcommand: -t/--test
[1]


$ dummy -t wibble foo
in dummy
in foo
[0]


$ dummy bar -h
usage: dummy bar [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar
in dummy
Traceback (most recent call last):
  ...
AttributeError: 'Namespace' object has no attribute 'test'
[1]
