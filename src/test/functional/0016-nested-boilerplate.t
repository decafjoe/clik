$ dummy -h
usage: dummy [-h] {foo,bar} ...

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {foo,bar}
    foo
    bar
[1]


$ dummy
usage: dummy [-h] {foo,bar} ...
dummy: error: the following arguments are required: {foo,bar}
[1]


$ dummy foo -h
usage: dummy foo [-h] {wibble,wobble} ...

optional arguments:
  -h, --help       show this help message and exit

subcommands:
  {wibble,wobble}
    wibble
    wobble
[1]


$ dummy foo
usage: dummy foo [-h] {wibble,wobble} ...
dummy foo: error: the following arguments are required: {wibble,wobble}
[1]


$ dummy foo wibble -h
usage: dummy foo wibble [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy foo wibble
wibble
[0]


$ dummy foo wobble -h
usage: dummy foo wobble [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy foo wobble
wobble
[0]


$ dummy bar -h
usage: dummy bar [-h] {wubble,flob} ...

optional arguments:
  -h, --help     show this help message and exit

subcommands:
  {wubble,flob}
    wubble
    flob
[1]


$ dummy bar
usage: dummy bar [-h] {wubble,flob} ...
dummy bar: error: the following arguments are required: {wubble,flob}
[1]


$ dummy bar wubble -h
usage: dummy bar wubble [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar wubble
wubble
[0]


$ dummy bar flob -h
usage: dummy bar flob [-h] {spam,ham,eggs} ...

optional arguments:
  -h, --help       show this help message and exit

subcommands:
  {spam,ham,eggs}
    spam
    ham
    eggs
[1]


$ dummy bar flob
usage: dummy bar flob [-h] {spam,ham,eggs} ...
dummy bar flob: error: the following arguments are required: {spam,ham,eggs}
[1]


$ dummy bar flob spam -h
usage: dummy bar flob spam [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar flob spam
spam
[0]


$ dummy bar flob ham -h
usage: dummy bar flob ham [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar flob ham
ham
[0]


$ dummy bar flob eggs -h
usage: dummy bar flob eggs [-h]

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar flob eggs
eggs
[0]
