import argparse
from pyls.core import pyls


def main():
    parser = argparse.ArgumentParser(description='List files and directories')
    parser.add_argument('-A', action='store_true', help='Include all files (including those starting with a dot)')
    parser.add_argument('-l', action='store_true', help='Use a long listing format')
    parser.add_argument('-r', action='store_true', help='Reverse the order of the listing')
    parser.add_argument('-t', action='store_true', help='Sort by modification time')
    parser.add_argument('--filter', help="Filter results based on 'file' or 'dir'")
    parser.add_argument('path', nargs='?', default='', help="Path to the directory or file")

    args = parser.parse_args()

    pyls(path=args.path, include_all=args.A, detailed=args.l, reverse=args.r, sort_by_time=args.t,
         filter_option=args.filter)


if __name__ == "__main__":
    main()
