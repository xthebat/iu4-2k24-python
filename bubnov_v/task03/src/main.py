import argparse
import os
from parse_smd import parse_file, create_new_smd


def main() -> None:
    parser = argparse.ArgumentParser(description='Command for modified smd file')
    parser.add_argument('file', type=str,
                        help='Name of the smd file to be modified')
    parser.add_argument('-dir', type=str, default=f'{os.path.dirname(__file__)}',
                        help='Directory where the file are stored (default: current directory)')

    args = parser.parse_args()
    create_new_smd(parse_file(args.file, args.dir))


if __name__ == '__main__':
    main()
