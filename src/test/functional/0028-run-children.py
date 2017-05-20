from clik import app, run_children


@app
def dummy():
    yield
    print('running setup code')
    try:
        child_exit_code = run_children()
    except Exception as e:
        print('exception:', e)
    else:
        print('child exit code:', child_exit_code)
    print('running tear down code')


@dummy
def foo():
    yield
    print('foo foo foo foo foo')


@dummy
def bar():
    yield
    print('bar bar bar bar bar')
    raise Exception('whoops')
