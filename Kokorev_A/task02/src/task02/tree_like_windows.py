import os.path
import argparse

lines = {
    "deep_line": "│ ",
    "item_line": "├─",
    "empty_line": "  ",
    "end_line": "└─"
}


class counter:
    dir_counter: int = 0
    item_counter: int = 0


def generate_tree(directory: str, req_depth: int, cur_depth: int):
    branch = [(os.path.basename(os.path.abspath(directory)))]
    if cur_depth > req_depth:
        return branch[0]
    list_of_items = os.listdir(directory)
    for item in list_of_items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            item = (generate_tree(item_path, req_depth, cur_depth + 1))
        branch.append(item)
    return branch


def print_tree(directory: str, tree, count: counter, layer_prefix=""):
    for index, item in enumerate(tree, 0):
        # Layer lines assembling
        layer_addition = lines["empty_line"]
        if index == len(tree) - 1:
            if len(tree) > 1:
                print("\033[37m{}".format(layer_prefix + lines["end_line"]), end='')
        else:
            if index > 0:
                print("\033[37m{}".format(layer_prefix + lines["item_line"]), end='')
                layer_addition = lines["deep_line"]
        # Items printing coloring and counting
        if isinstance(item, list):
            print_tree(os.path.join(directory, item[0]), item, count, layer_prefix + layer_addition)
        else:
            item_path = directory
            if index > 0:
                item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                print("\033[34m{}".format(item))
                count.dir_counter += 1
            else:
                print("\033[32m{}".format(item))
                count.item_counter += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="displays the directory structure as a tree with a specified depth")
    parser.add_argument("-L", "--depth", type=int, default=1,
                        help="Depth (nesting level) to display")
    parser.add_argument("directory", type=str, help="Path to the directory")
    args = parser.parse_args()
    count = counter()
    print_tree(args.directory, generate_tree(args.directory, args.depth, 1), count)
    print("\033[37m{}".format(""), count.dir_counter - 1, " directories, ", count.item_counter, " files")
