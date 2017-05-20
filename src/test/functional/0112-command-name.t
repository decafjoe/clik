$ dummy -h
usage: dummy [-h] {baz,qux} ...

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {baz,qux}
    baz
    qux
[1]


$ dummy foo
usage: dummy [-h] {baz,qux} ...
dummy: error: argument {baz,qux}: invalid choice: 'foo' (choose from 'baz', 'qux')
[1]


$ dummy bar
usage: dummy [-h] {baz,qux} ...
dummy: error: argument {baz,qux}: invalid choice: 'bar' (choose from 'baz', 'qux')
[1]


$ dummy baz
in foo / baz
[0]


$ dummy qux
in bar / qux
[0]
