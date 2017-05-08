$ dummy -h
usage: dummy [-h] {bar,foo} ...

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {bar,foo}
    foo
    bar
[1]


$ dummy
usage: dummy [-h] {bar,foo} ...
dummy: error: the following arguments are required: {bar,foo}
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
usage: dummy bar [-h] {flob,wubble} ...

optional arguments:
  -h, --help     show this help message and exit

subcommands:
  {flob,wubble}
    wubble
    flob
[1]


$ dummy bar
usage: dummy bar [-h] {flob,wubble} ...
dummy bar: error: the following arguments are required: {flob,wubble}
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
usage: dummy bar flob [-h] {eggs,ham,spam} ...

optional arguments:
  -h, --help       show this help message and exit

subcommands:
  {eggs,ham,spam}
    spam
    ham
    eggs
[1]


$ dummy bar flob
usage: dummy bar flob [-h] {eggs,ham,spam} ...
dummy bar flob: error: the following arguments are required: {eggs,ham,spam}
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
