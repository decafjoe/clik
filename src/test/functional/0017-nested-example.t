$ dummy -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
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
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy [-h] {bar,foo} ...
dummy: error: the following arguments are required: {bar,foo}
[1]


$ dummy foo -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy foo [-h] {wibble,wobble} ...

Foo all the things.

optional arguments:
  -h, --help       show this help message and exit

subcommands:
  {wibble,wobble}
    wibble         Wibble this, that, and the other.
    wobble         Wobble all the way to the bank.
[1]


$ dummy foo
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy foo [-h] {wibble,wobble} ...
dummy foo: error: the following arguments are required: {wibble,wobble}
[1]


$ dummy foo wibble -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy foo wibble [-h]

Wibble this, that, and the other.

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy foo wibble
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
running dummy setup code
running foo setup code
wibble wibble
running foo teardown code
running dummy teardown code
[0]


$ dummy foo wobble -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy foo wobble [-h]

Wobble all the way to the bank.

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy foo wobble
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
running dummy setup code
running foo setup code
wobble wobble
running foo teardown code
running dummy teardown code
[0]


$ dummy bar -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy bar [-h] {flob,wubble} ...

Bar all over the place.

optional arguments:
  -h, --help     show this help message and exit

subcommands:
  {flob,wubble}
    wubble       Wubble wubble, toil and trouble.
    flob         Flob (whatever that is).
[1]


$ dummy bar
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy bar [-h] {flob,wubble} ...
dummy bar: error: the following arguments are required: {flob,wubble}
[1]


$ dummy bar wubble -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy bar wubble [-h]

Wubble wubble, toil and trouble.

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar wubble
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
running dummy setup code
running bar setup code
wubble wubble
running bar teardown code
running dummy teardown code
[0]


$ dummy bar flob -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy bar flob [-h] {eggs,ham,spam} ...

Flob (whatever that is).

optional arguments:
  -h, --help       show this help message and exit

subcommands:
  {eggs,ham,spam}
    spam           Spam + 1.
    ham            Everybody's having ham!
    eggs           Some single-line description of the eggs subcommand.
[1]


$ dummy bar flob
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy bar flob [-h] {eggs,ham,spam} ...
dummy bar flob: error: the following arguments are required: {eggs,ham,spam}
[1]


$ dummy bar flob spam -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy bar flob spam [-h]

Spam + 1.

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar flob spam
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
running dummy setup code
running bar setup code
running flob setup code
spam spam
running flob teardown code
running bar teardown code
running dummy teardown code
[0]


$ dummy bar flob ham -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy bar flob ham [-h]

Everybody's having ham!

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar flob ham
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
running dummy setup code
running bar setup code
running flob setup code
ham ham
running flob teardown code
running bar teardown code
running dummy teardown code
[0]


$ dummy bar flob eggs -h
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
usage: dummy bar flob eggs [-h]

Some single-line description of the eggs subcommand.

optional arguments:
  -h, --help  show this help message and exit
[1]


$ dummy bar flob eggs
configuring dummy parser
configuring foo parser
configuring wibble parser
configuring wobble parser
configuring bar parser
configuring wubble parser
configuring flob parser
configuring spam parser
configuring ham parser
configuring eggs parser
running dummy setup code
running bar setup code
running flob setup code
eggs eggs
running flob teardown code
running bar teardown code
running dummy teardown code
[0]
