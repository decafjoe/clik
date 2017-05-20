from clik import app, args, parser


@app
def dummy():
    print('configuring dummy parser')
    yield


@dummy.bare
def dummy_bare():
    print('configuring dummy bare parser')
    group = parser.add_mutually_exclusive_group()
    yield


@dummy
def foo():
    print('configuring foo parser')
    yield


@dummy
def bar():
    print('configuring bar parser')
    yield
