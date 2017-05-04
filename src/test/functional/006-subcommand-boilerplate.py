from clik import app


@app
def dummy():
    """Program with subcommands."""
    yield


@dummy
def foo():
    """Foo all the things."""
    yield


@dummy
def bar():
    """Bar all over the place."""
    yield
