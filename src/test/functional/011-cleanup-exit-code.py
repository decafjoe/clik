from clik import app


@app
def dummy():
    yield
    print('running setup code')
    yield
    print('running tear down code')
    yield 7


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
    yield 42
