from clik import app


@app
def dummy():
    """Program with subcommands."""
    print('configuring dummy parser')
    yield
    print('running dummy setup code')
    yield
    print('running dummy teardown code')


@dummy
def foo():
    """Foo all the things."""
    print('configuring foo parser')
    yield
    print('running foo setup code')
    yield
    print('running foo teardown code')


@foo
def wibble():
    """Wibble this, that, and the other."""
    print('configuring wibble parser')
    yield
    print('wibble wibble')


@foo
def wobble():
    """Wobble all the way to the bank."""
    print('configuring wobble parser')
    yield
    print('wobble wobble')


@dummy
def bar():
    """Bar all over the place."""
    print('configuring bar parser')
    yield
    print('running bar setup code')
    yield
    print('running bar teardown code')


@bar
def wubble():
    """Wubble wubble, toil and trouble."""
    print('configuring wubble parser')
    yield
    print('wubble wubble')


@bar
def flob():
    """Flob (whatever that is)."""
    print('configuring flob parser')
    yield
    print('running flob setup code')
    yield
    print('running flob teardown code')


@flob
def spam():
    """Spam + 1."""
    print('configuring spam parser')
    yield
    print('spam spam')


@flob
def ham():
    """Everybody's having ham!"""
    print('configuring ham parser')
    yield
    print('ham ham')


@flob
def eggs():
    """Some single-line description of the eggs subcommand."""
    print('configuring eggs parser')
    yield
    print('eggs eggs')
