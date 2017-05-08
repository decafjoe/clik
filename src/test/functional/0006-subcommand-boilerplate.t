$ dummy -h
usage: dummy [-h] {bar,foo} ...

Program with subcommands.

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {bar,foo}
    foo       Foo all the things.
    bar       Bar all over the place.
[1]


$ dummy
usage: dummy [-h] {bar,foo} ...
dummy: error: the following arguments are required: {bar,foo}
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
