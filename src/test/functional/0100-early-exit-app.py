from clik import app


@app
def dummy():
    print('configuring parser for dummy')
    yield 42


@dummy
def foo():
    print('configuring parser for foo')
    yield


@dummy
def bar():
    print('configuring parser for bar')
    yield
