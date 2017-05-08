from clik import app


@app
def dummy():
    yield


# Note: These lines aren't necessary for functional tests. They're
#       here in the first one only to demonstrate how to invoke clik
#       applications.
if __name__ == '__main__':
    dummy.main()
