from clik import app


@app
def dummy():
    print('configuring parser for dummy')
    yield
    print('in dummy')


@dummy.bare
def dummy_bare():
    print('configuring parser for dummy bare')
    yield 42
    print('in dummy bare')
