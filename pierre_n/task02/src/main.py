import argparse
from task02.tree import get_directory_tree, display_tree

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display directory tree.")
    parser.add_argument("directory", type=str, help="Directory path")
    parser.add_argument("-L", "--max-depth", type=int, default=None, help="Maximum depth of the directory tree to display")
    args = parser.parse_args()

    directory_path = args.directory
    max_depth = args.max_depth

    tree = get_directory_tree(directory_path)
    display_tree(tree, max_depth=max_depth)

