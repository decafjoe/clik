from clik import app, catch


@app
def dummy():
    yield
    print('running setup code')
    child_exit_code, exception = (yield catch)
    print('exception:', exception)
    print('running tear down code')


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
    raise Exception('whoops')
