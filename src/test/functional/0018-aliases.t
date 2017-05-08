$ dummy -h
usage: dummy [-h] {foo,bar,baz} ...

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  {foo,bar,baz}
    foo (f)
    bar (b, ba)
    baz (bz, another-alias, a_third)
[1]


$ dummy foo
foo foo foo foo foo
[0]


$ dummy f
foo foo foo foo foo
[0]


$ dummy bar
bar bar bar bar bar
[0]


$ dummy b
bar bar bar bar bar
[0]


$ dummy ba
bar bar bar bar bar
[0]


$ dummy baz
baz baz baz baz baz
[0]


$ dummy bz
baz baz baz baz baz
[0]


$ dummy another-alias
baz baz baz baz baz
[0]


$ dummy a_third
baz baz baz baz baz
[0]
