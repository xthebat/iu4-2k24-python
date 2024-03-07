import argparse
from scripts.tree import gen_tree, print_tree

def main():
    parser = argparse.ArgumentParser(description="Catch your path and level")
    parser.add_argument("path", type=str, help="Path to the directory")
    parser.add_argument("lvl", type=int, help="Nesting level")
    args = parser.parse_args()
    dir_tree = gen_tree(args.path, args.lvl)
    print_tree(dir_tree)

if __name__ == '__main__':
    main()