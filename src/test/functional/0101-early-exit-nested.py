from clik import app


@app
def dummy():
    print('configuring parser for dummy')
    yield


@dummy
def foo():
    print('configuring parser for foo')
    yield


@foo
def wibble():
    print('configuring parser for wibble')
    yield


@foo
def wobble():
    print('configuring parser for wobble')
    yield 42


@dummy
def bar():
    print('configuring parser for bar')
    yield


@bar
def wubble():
    print('configuring parser for wubble')
    yield


@bar
def flob():
    print('configuring parser for flob')
    yield
