from clik import app, parser


@app
def dummy():
    parser.add_argument('test', nargs=1)
    yield
