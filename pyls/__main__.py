import argparse
from pyls.core import pyls


def main():
    # Create a parser and disable the default help option
    parser = argparse.ArgumentParser(description='List files and directories', add_help=False)

    # Manually add the --help option
    parser.add_argument('--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit')

    parser.add_argument('-A', action='store_true', help='Include all files (including those starting with a dot)')
    parser.add_argument('-l', action='store_true', help='Use a long listing format')
    parser.add_argument('-r', action='store_true', help='Reverse the order of the listing')
    parser.add_argument('-t', action='store_true', help='Sort by modification time')
    parser.add_argument('-h', action='store_true', help='Show human-readable sizes')
    parser.add_argument('--filter', help="Filter results based on 'file' or 'dir'")
    parser.add_argument('path', nargs='?', default='', help="Path to the directory or file")

    args = parser.parse_args()

    pyls(path=args.path, include_all=args.A, detailed=args.l, reverse=args.r, sort_by_time=args.t,
         human_readable=args.h, filter_option=args.filter)


if __name__ == "__main__":
    main()
