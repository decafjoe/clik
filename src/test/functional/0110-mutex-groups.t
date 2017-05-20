$ dummy -h
usage: dummy [-h] [-a | -b] {foo,bar} ...

optional arguments:
  -h, --help  show this help message and exit
  -a
  -b

subcommands:
  {foo,bar}
    foo
    bar
[1]


$ dummy foo -h
usage: dummy foo [-h] [-c | -d]

optional arguments:
  -h, --help  show this help message and exit
  -c
  -d
[1]


$ dummy foo
in dummy, a: False b: False
in foo, a: False b: False c: False d: False
[0]


$ dummy -a foo
in dummy, a: True b: False
in foo, a: True b: False c: False d: False
[0]


$ dummy -b foo
in dummy, a: False b: True
in foo, a: False b: True c: False d: False
[0]


$ dummy -a -b foo
usage: dummy [-h] [-a | -b] {foo,bar} ...
dummy: error: argument -b: not allowed with argument -a
[1]


$ dummy foo -c
in dummy, a: False b: False
in foo, a: False b: False c: True d: False
[0]


$ dummy foo -d
in dummy, a: False b: False
in foo, a: False b: False c: False d: True
[0]


$ dummy foo -c -d
usage: dummy foo [-h] [-c | -d]
dummy foo: error: argument -d: not allowed with argument -c
[1]


$ dummy bar -h
usage: dummy bar [-h] [-c | -d]

optional arguments:
  -h, --help  show this help message and exit
  -c
  -d
[1]


$ dummy bar
in dummy, a: False b: False
in bar, a: False b: False c: False d: False
[0]


$ dummy bar -c
in dummy, a: False b: False
in bar, a: False b: False c: True d: False
[0]


$ dummy bar -d
in dummy, a: False b: False
in bar, a: False b: False c: False d: True
[0]


$ dummy bar -c -d
usage: dummy bar [-h] [-c | -d]
dummy bar: error: argument -d: not allowed with argument -c
[1]
