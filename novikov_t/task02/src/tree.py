import os
import argparse


BRANCH_END = "└── " 
BRANCH_LEFT = "│   "
BRANCH_RIGHT = "├── "
BRANCH_SPACE = "    "


def generate_tree(directory, req_depth, current_depth=1):
    tree = []
    # get directory name
    tree.append((os.path.basename(os.path.abspath(directory))))
    if current_depth > req_depth:
        return tree[0]
    # get the list of the items contained in directory
    list_of_items = os.listdir(directory)
    for item in list_of_items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            item = (generate_tree(item_path, req_depth,
                                  current_depth + 1))
        tree.append(item)
    return tree


def print_tree(tree, decor_prefix=""):
    print(tree.pop(0))
    for index, item in enumerate(tree, 1):
        if index == len(tree):
            print(decor_prefix + BRANCH_END, end='')
            decor_plus = BRANCH_SPACE
        else:
            print(decor_prefix + BRANCH_RIGHT, end='')
            decor_plus = BRANCH_LEFT
        if isinstance(item, list):
            print_tree(item, decor_prefix + decor_plus)
        else:
            print(item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="displays the directory structure as a tree with a specified depth")
    parser.add_argument("-L", "--depth", type=int, default=1,
                        help="Depth (nesting level) to display")
    parser.add_argument("directory", type=str, help="Path to the directory")

    args = parser.parse_args()
    print_tree(generate_tree(args.directory, args.depth))
