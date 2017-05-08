from clik import app


@app
def dummy():
    yield
    print('in dummy')
    yield
    print('cleanup dummy')


@dummy
def foo():
    yield
    print('in foo')
    yield
    print('cleanup foo')


@foo
def wibble():
    yield
    print('in wibble')


@foo
def wobble():
    yield
    print('in wobble')


@dummy
def bar():
    yield
    print('in bar')
    yield 42
    print('cleanup bar')


@bar
def wubble():
    yield
    print('in wubble')


@bar
def flob():
    yield
    print('in flob')
