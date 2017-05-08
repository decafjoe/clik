from clik import app, args, parser


@app
def dummy():
    parser.add_argument(
        '-f',
        '--fail',
        action='store_true',
        default=False,
        help='fail without invoking the child command',
    )

    yield

    if args.fail:
        yield 42


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
