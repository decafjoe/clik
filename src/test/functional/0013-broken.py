from clik import app


@app
def dummy():
    yield
    print('running setup code')
    try:
        yield
    except Exception as e:
        print('running tear down code')
        print(e)


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
    raise Exception('whoops')
