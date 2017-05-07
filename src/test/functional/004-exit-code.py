from clik import app


@app
def dummy():
    print('configuring parser')
    yield
    print('running code')
    yield 42
