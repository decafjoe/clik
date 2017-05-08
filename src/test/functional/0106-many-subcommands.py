from clik import app


@app
def dummy():
    yield


@dummy
def foo():
    yield


@dummy
def bar():
    yield


@dummy
def baz():
    yield


@dummy
def qux():
    yield
