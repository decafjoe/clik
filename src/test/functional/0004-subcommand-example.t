$ dummy -h
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy [-h] [-v] {foo,bar} ...

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  output more stuff

subcommands:
  {foo,bar}
    foo
    bar
[1]


$ dummy foo -h
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy foo [-h] [-l]

optional arguments:
  -h, --help  show this help message and exit
  -l, --loud  do it louder
[1]


$ dummy bar -h
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy bar [-h] [-f]

optional arguments:
  -h, --help  show this help message and exit
  -f, --fast  do it faster
[1]


$ dummy
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy [-h] [-v] {foo,bar} ...
dummy: error: the following arguments are required: {foo,bar}
[1]


$ dummy foo
configuring top-level parser
configuring foo parser
configuring bar parser
running the code after the yield in "dummy"
running foo
foo foo foo foo foo
[0]


$ dummy --verbose foo
configuring top-level parser
configuring foo parser
configuring bar parser
running the code after the yield in "dummy"
running foo
foo foo foo foo foo foo foo foo foo foo
[0]


$ dummy foo --loud
configuring top-level parser
configuring foo parser
configuring bar parser
running the code after the yield in "dummy"
running foo
FOO FOO FOO FOO FOO
[0]


$ dummy --verbose foo --loud
configuring top-level parser
configuring foo parser
configuring bar parser
running the code after the yield in "dummy"
running foo
FOO FOO FOO FOO FOO FOO FOO FOO FOO FOO
[0]


$ dummy foo --verbose
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy [-h] [-v] {foo,bar} ...
dummy: error: unrecognized arguments: --verbose
[1]


$ dummy bar
configuring top-level parser
configuring foo parser
configuring bar parser
running the code after the yield in "dummy"
running bar
bar bar bar bar bar
[0]


$ dummy --verbose bar
configuring top-level parser
configuring foo parser
configuring bar parser
running the code after the yield in "dummy"
running bar
bar bar bar bar bar bar bar bar bar bar
[0]


$ dummy bar --fast
configuring top-level parser
configuring foo parser
configuring bar parser
running the code after the yield in "dummy"
running bar
barbarbarbarbar
[0]


$ dummy --verbose bar --fast
configuring top-level parser
configuring foo parser
configuring bar parser
running the code after the yield in "dummy"
running bar
barbarbarbarbarbarbarbarbarbar
[0]


$ dummy bar --verbose
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy [-h] [-v] {foo,bar} ...
dummy: error: unrecognized arguments: --verbose
[1]
