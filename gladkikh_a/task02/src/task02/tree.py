import os
import argparse

PIPE = "|"
ELBOW = "`-- "
TEE = "|-- "
PIPE_PREFIX = "|   "
SPACE_PREFIX = "    "

def generate_tree(directory, depth):
    tree = []
    tree_head(directory, tree)
    tree_body(directory, tree, depth)
    return tree

def tree_head(directory, tree):
    tree.append(f"{directory}")
    tree.append(PIPE)

def tree_body(directory, tree, depth, prefix=""):
    if depth == 0:
        return

    entries = os.listdir(directory)
    entries = sorted(entries, key=lambda entry: os.path.isdir(os.path.join(directory, entry)))
    entries_count = len(entries)

    for index, entry in enumerate(entries):
        connector = ELBOW if index == entries_count - 1 else TEE
        full_path = os.path.join(directory, entry)

        if os.path.isdir(full_path):
            add_directory(full_path, tree, index, entries_count, prefix, connector, depth)
        else:
            add_file(full_path, tree, prefix, connector)

def add_directory(entry, tree, index, entries_count, prefix, connector, depth):
    tree.append(prefix + connector + os.path.basename(entry))
    if index != entries_count - 1:
        tree_body(entry, tree, depth - 1, prefix + PIPE_PREFIX)
    else:
        tree_body(entry, tree, depth - 1, prefix + SPACE_PREFIX)

def add_file(entry, tree, prefix, connector):
    tree.append(prefix + connector + os.path.basename(entry))

def print_tree(tree, depth):
    for entry in tree:
        print(entry)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Displays the directory structure as a tree with a specified depth")
    parser.add_argument("-H", "--depth", type=int, default=1,
                        help="Depth (nesting level) to display")
    parser.add_argument("directory", type=str, help="Path to the directory")

    args = parser.parse_args()

    tree = generate_tree(args.directory, args.depth)
    print_tree(tree, args.depth)
