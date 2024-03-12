from flags import args
from tree import print_tree


def main():
    print_tree(args.dir, args.nest)


if __name__ == '__main__':
    main()
