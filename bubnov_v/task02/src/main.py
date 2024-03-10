import argparse
from tree import create_tree, output_tree, total_number_element


def main():
    parser = argparse.ArgumentParser(description='Tree command implementation')
    parser.add_argument('function', type=str, help='Calling function')
    parser.add_argument('-L', type=int, default=float('inf'),
                        help='Max display depth of the directory tree (default: infinity)')
    parser.add_argument('directory', type=str, default='.',
                        help='Directory from which tree start (default: current directory)')
    args = parser.parse_args()

    if args.function == 'tree':
        total_number_element(output_tree(create_tree(args.directory, args.L), args.directory, True))
    else:
        print('Use -h to get information about available arguments and options')


if __name__ == '__main__':
    main()
