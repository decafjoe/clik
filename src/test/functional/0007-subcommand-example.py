from clik import app, args, parser


@app
def dummy():
    print('configuring top-level parser')
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output more stuff',
    )

    yield

    print('running the code after the yield in "dummy"')


@dummy
def foo():
    print('configuring foo parser')
    parser.add_argument(
        '-l',
        '--loud',
        action='store_true',
        default=False,
        help='do it louder',
    )

    yield

    print('running foo')
    msg = 'FOO' if args.loud else 'foo'
    number = 10 if args.verbose else 5
    print(' '.join([msg for _ in range(number)]))


@dummy
def bar():
    print('configuring bar parser')
    parser.add_argument(
        '-f',
        '--fast',
        action='store_true',
        default=False,
        help='do it faster',
    )

    yield

    print('running bar')
    join_character = '' if args.fast else ' '
    number = 10 if args.verbose else 5
    print(join_character.join(['bar' for _ in range(number)]))

    yield 42
