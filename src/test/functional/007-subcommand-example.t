$ dummy -h
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy [-h] [-v] {bar,foo} ...

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  output more stuff

subcommands:
  {bar,foo}
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
  -l, --loud  foo louder
[1]


$ dummy bar -h
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy bar [-h] [-f]

optional arguments:
  -h, --help  show this help message and exit
  -f, --fast  bar faster
[1]


$ dummy
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy [-h] [-v] {bar,foo} ...
dummy: error: the following arguments are required: {bar,foo}
[1]


$ dummy foo
configuring top-level parser
configuring foo parser
configuring bar parser
invoking the code after the yield in "dummy"
invoking foo
foo foo foo foo foo
[0]


$ dummy --verbose foo
configuring top-level parser
configuring foo parser
configuring bar parser
invoking the code after the yield in "dummy"
invoking foo
foo foo foo foo foo foo foo foo foo foo
[0]


$ dummy foo --loud
configuring top-level parser
configuring foo parser
configuring bar parser
invoking the code after the yield in "dummy"
invoking foo
FOO FOO FOO FOO FOO
[0]


$ dummy --verbose foo --loud
configuring top-level parser
configuring foo parser
configuring bar parser
invoking the code after the yield in "dummy"
invoking foo
FOO FOO FOO FOO FOO FOO FOO FOO FOO FOO
[0]


$ dummy foo --verbose
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy [-h] [-v] {bar,foo} ...
dummy: error: unrecognized arguments: --verbose
[1]


$ dummy bar
configuring top-level parser
configuring foo parser
configuring bar parser
invoking the code after the yield in "dummy"
invoking bar
bar bar bar bar bar
[42]


$ dummy --verbose bar
configuring top-level parser
configuring foo parser
configuring bar parser
invoking the code after the yield in "dummy"
invoking bar
bar bar bar bar bar bar bar bar bar bar
[42]


$ dummy bar --fast
configuring top-level parser
configuring foo parser
configuring bar parser
invoking the code after the yield in "dummy"
invoking bar
barbarbarbarbar
[42]


$ dummy --verbose bar --fast
configuring top-level parser
configuring foo parser
configuring bar parser
invoking the code after the yield in "dummy"
invoking bar
barbarbarbarbarbarbarbarbarbar
[42]


$ dummy bar --verbose
configuring top-level parser
configuring foo parser
configuring bar parser
usage: dummy [-h] [-v] {bar,foo} ...
dummy: error: unrecognized arguments: --verbose
[1]
