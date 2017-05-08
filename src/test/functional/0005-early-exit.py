from clik import app


@app
def dummy():
    print('this will be printed...')
    yield 42
    print('...but this will not')
