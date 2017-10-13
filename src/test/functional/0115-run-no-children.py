from clik import app, run_children


@app
def dummy():
    yield
    yield run_children()
