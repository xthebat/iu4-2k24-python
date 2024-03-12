import argparse
from tree import create_tree, output_tree


# Creating a parser for incoming arguments and options
def main():
    parser = argparse.ArgumentParser(description='command line')
    parser.add_argument('command', type=str, help='Command name')
    parser.add_argument('-L', type=int, help='Depth of the directory')
    parser.add_argument('indir', type=str, default='.', help='Tree stand directory')
    args = parser.parse_args()
    print(args.command, args.L, args.indir)
    # Start function "tree"
    if args.command == 'tree':
        output_tree(create_tree(args.indir, args.L), args.indir)
    else:
        print('Unknown command')

    if __name__ == '__main__':
        main()

# ЯЯЯЯ\Бомонка\Python\iu4-2k24-python\blokhin_m\task02\src\task02
