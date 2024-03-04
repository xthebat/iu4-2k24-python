from flags import args
from tree import tree


def main():
    tree(args.dir, args.nest)


if __name__ == '__main__':
    main()
