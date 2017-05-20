from clik import app, args, parser


@app
def dummy():
    print('configuring dummy parser')
    yield


@dummy.bare
def dummy_bare():
    print('configuring dummy bare parser')
    parser.add_argument(
        'test',
        nargs=1,
    )
    yield


@dummy
def foo():
    print('configuring foo parser')
    yield


@dummy
def bar():
    print('configuring bar parser')
    yield
