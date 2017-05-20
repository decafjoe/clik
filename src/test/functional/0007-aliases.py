from clik import app


@app
def dummy():
    yield


@dummy(alias='f')
def foo():
    yield
    print('foo foo foo foo foo')


@dummy(aliases=('b', 'ba'))
def bar():
    yield
    print('bar bar bar bar bar')


@dummy(alias='bz', aliases=('another-alias', 'a_third'))
def baz():
    yield
    print('baz baz baz baz baz')
