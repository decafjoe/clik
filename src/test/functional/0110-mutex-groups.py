from clik import app, args, parser


@app
def dummy():
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', action='store_true', default=False)
    group.add_argument('-b', action='store_true', default=False)
    yield
    print('in dummy, a:', args.a, 'b:', args.b)


@dummy
def foo():
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', action='store_true', default=False)
    group.add_argument('-d', action='store_true', default=False)
    yield
    print('in foo, a:', args.a, 'b:', args.b, 'c:', args.c, 'd:', args.d)


@dummy
def bar():
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', action='store_true', default=False)
    group.add_argument('-d', action='store_true', default=False)
    yield
    print('in bar, a:', args.a, 'b:', args.b, 'c:', args.c, 'd:', args.d)
