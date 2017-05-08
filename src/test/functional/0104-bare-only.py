from clik import app


@app
def dummy():
    yield


@dummy.bare
def dummy_bare():
    yield
    yield 42
