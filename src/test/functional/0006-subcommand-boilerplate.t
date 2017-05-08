$ dummy -h
usage: dummy [-h] {foo,bar} ...

Program with subcommands.

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {foo,bar}
    foo       Foo all the things.
    bar       Bar all over the place.
[1]


$ dummy
usage: dummy [-h] {foo,bar} ...
dummy: error: the following arguments are required: {foo,bar}
[1]


$ dummy foo -h
usage: dummy foo [-h]

Foo all the things.

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy foo
foo
[0]


$ dummy bar -h
usage: dummy bar [-h]

Bar all over the place.

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar
bar
[0]
