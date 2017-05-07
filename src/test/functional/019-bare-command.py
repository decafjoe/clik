from clik import app, args, parser


@app
def dummy():
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
    )
    yield
    print('in dummy, args.verbose:', args.verbose)


@dummy.bare
def dummy_bare():
    parser.add_argument(
        '-t',
        '--test',
        action='store_true',
        default=False,
    )
    yield
    print('in dummy_bare, args.verbose:', args.verbose)
    print('in dummy_bare, args.test:', args.test)


@dummy
def foo():
    yield
    print('in foo, args.verbose:', args.verbose)


@dummy
def bar():
    yield
    print('in bar, args.verbose:', args.verbose)
    print('in bar, args.test:', args.test)
