from clik import app


@app
def dummy():
    yield
    yield 42
