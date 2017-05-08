from clik import app


@app
def dummy():
    yield
    print('running setup code')
    child_exit_code = (yield)
    print('child exit code:', child_exit_code)
    print('running tear down code')


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
    yield 42
