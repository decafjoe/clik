from clik import app


@app
def dummy():
    """
    A simple test application to demonstrate how docstrings are used.

    The first part of the docstring will be used as the ``description``
    argument to the argument parser. If there is a blank line and then more
    text, as there is in this docstring, all the text following the blank
    line is used as the ``epilog``.
    """
    yield
