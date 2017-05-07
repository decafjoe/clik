from clik import app


@app
def dummy():
    """Program with subcommands."""
    yield


@dummy
def foo():
    """Foo all the things."""
    yield
    print('foo')


@dummy
def bar():
    """Bar all over the place."""
    yield
    print('bar')
