$ dummy -h
usage: dummy [-h] {command} ...

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {command}
    foo
    bar
    baz
    qux
[1]


$ dummy
usage: dummy [-h] {command} ...
dummy: error: the following arguments are required: {command}
[1]
