from argparse import ArgumentParser, SUPPRESS


def do_something(options):
    '''A function that does something'''
    print(str(options))


if __name__ == '__main__':
    prog = "test_ArgParse"
    help_string = """\
    Purpose: Check how to use ArgParse
    """

    parser = ArgumentParser (
        description=help_string, prog=prog,
    )

    # NOTES: Default are the following
    # * action = 'store'
    # * type = 'str'
    # * metavar = variable where option is stored

    # Arguments
    parser.add_argument('arg1')
    parser.add_argument('arg_int', type=int)  # check type
    parser.add_argument('arg3', type=int, metavar='INT')  # name in help
    parser.add_argument('other_args', type=int, nargs='*')  # Optional args

    # Modes
    modes = parser.add_argument_group ("Modes")
    modes.add_argument (
        "-v", "--verbose",
        action="store_true", dest="verbose", default=False,
        help="Display additional information messages"
    )
    modes.add_argument (
        "--debug", action="store_true", help=SUPPRESS
        # Note: by default, 'dest' is the name of option with '--'
        # Note: default value for "store_true" is False
    )

    options = parser.parse_args ()
    do_something(options)
