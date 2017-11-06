$ dummy -h
usage: dummy [-h] {foo,bar} ...

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {foo,bar}
    foo
    bar
[1]


$ dummy foo spam
spam
[0]


$ dummy foo spam -v --foo eggs
usage: dummy [-h] {foo,bar} ...
dummy: error: unrecognized arguments: -v --foo eggs
[1]


$ dummy foo ham
unknown args: []
[0]


$ dummy foo ham -v --foo eggs
unknown args: ['-v', '--foo', 'eggs']
[0]

$ dummy bar
unknown args: []
[0]


$ dummy bar -v --foo eggs
unknown args: ['-v', '--foo', 'eggs']
[0]
