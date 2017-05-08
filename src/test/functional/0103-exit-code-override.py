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
    yield 0


@foo
def wibble():
    yield
    print('in wibble')


@foo
def wobble():
    yield
    print('in wobble')
    yield 42


@dummy
def bar():
    yield
    print('in bar')
    yield
    print('cleanup bar')
    yield 7


@bar
def wubble():
    yield
    print('in wubble')


@bar
def flob():
    yield
    print('in flob')
    yield 42
