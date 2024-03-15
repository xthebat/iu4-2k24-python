import sys
import argparse as argp


sys.path.append('/Users/yaao20u291/Library/Mobile Documents/com~apple~CloudDocs/code/Python/iu4-2k24-python/iu4-2k24-python/yakimov_a/task02')

from scripts.tree import gen_tree, print_tree

# from ..scripts.arg_parser import args
# from ..scripts.tree import gen_tree

def main():
    parser = argp.ArgumentParser(description="Catch your path and level")
    parser.add_argument("path", type=str, help="Path to the directory")
    parser.add_argument("lvl", type=int, help="Nesting level")
    args = parser.parse_args()
    # print_tree(gen_tree(args.path, args.lvl))
    dir_tree = gen_tree(args.path, args.lvl)
    print_tree(dir_tree)

if __name__ == '__main__':
    main()