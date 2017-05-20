from clik import app, args, parser


@app
def dummy():
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
        help='output diagnostic information',
    )

    yield

    if args.verbose:
        print('you chose verbose')
