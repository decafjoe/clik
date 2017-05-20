$ dummy -h
usage: dummy [-h] [-f] {foo,bar} ...

optional arguments:
  -h, --help  show this help message and exit
  -f, --fail  fail without invoking the child command

subcommands:
  {foo,bar}
    foo
    bar
[1]


$ dummy foo
foo foo foo foo foo
[0]


$ dummy -f foo
[7]


$ dummy bar
bar bar bar bar bar
[42]


$ dummy -f bar
[7]
