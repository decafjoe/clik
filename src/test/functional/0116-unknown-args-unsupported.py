from clik import app, parser, unknown_args


@app
def dummy():
    parser.allow_unknown_args()
    yield


@dummy
def foo():
    yield
