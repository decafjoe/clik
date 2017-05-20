from clik import app, args, parser


@app
def dummy():
    yield
    print('in dummy')


@dummy.bare
def dummy_bare():
    parser.add_argument(
        '-t',
        '--test',
        default='wibble',
    )
    yield
    print('in dummy_bare, args.test:', args.test)


@dummy
def foo():
    yield
    print('in foo')


@dummy
def bar():
    yield
    print('in bar, args.test:', args.test)
