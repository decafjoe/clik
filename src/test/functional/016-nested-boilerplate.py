from clik import app


@app
def dummy():
    yield


@dummy
def foo():
    yield


@foo
def wibble():
    yield
    print('wibble')


@foo
def wobble():
    yield
    print('wobble')


@dummy
def bar():
    yield


@bar
def wubble():
    yield
    print('wubble')


@bar
def flob():
    yield


@flob
def spam():
    yield
    print('spam')


@flob
def ham():
    yield
    print('ham')


@flob
def eggs():
    yield
    print('eggs')
