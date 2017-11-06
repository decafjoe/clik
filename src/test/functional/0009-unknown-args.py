from clik import app, parser, unknown_args


@app
def dummy():
    yield


@dummy
def foo():
    yield


@foo
def spam():
    yield
    print('spam')


@foo
def ham():
    parser.allow_unknown_args()
    yield
    print('unknown args:', unknown_args)


@dummy
def bar():
    parser.allow_unknown_args()
    yield
    print('unknown args:', unknown_args)
