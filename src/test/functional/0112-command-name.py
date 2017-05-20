from clik import app


@app
def dummy():
    yield


@dummy(name='baz')
def foo():
    yield
    print('in foo / baz')


@dummy(name='qux')
def bar():
    yield
    print('in bar / qux')
