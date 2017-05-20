from clik import app


@app
def dummy():
    yield


@dummy
def foo():
    yield
    print('foo')


@dummy
def bar():
    yield
    print('bar')
    yield 42
