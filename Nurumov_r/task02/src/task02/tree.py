import os
import argparse
from colorama import init, Fore

BRANCH_END = "└── "
BRANCH_LEFT = "│   "
BRANCH_RIGHT = "├── "
BRANCH_SPACE = "    "


def explore_directory(directory: str, max_depth: int, depth: int = 1) -> tuple[list, int, int]:
    """
    Function to collect all the files, directories in the given directory

    :param directory: Directory to explore
    :param max_depth: Maximum depth of exploration
    :param depth: Current depth of exploration
    :return: List of directories and files, number of directories, number files
    """

    tree = []
    directories_count, files_count = 0, 0

    tree.append((os.path.basename(os.path.abspath(directory))))
    if depth > max_depth:
        return tree, directories_count, files_count
    try:
        list_of_items = os.listdir(directory)
    except PermissionError:
        print(f"{Fore.RED}ERROR: Permission denied")
        return

    for item in list_of_items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            item, sub_directories_count, sub_files_count = explore_directory(
                item_path, max_depth, depth + 1)
            directories_count += sub_directories_count + 1
            files_count += sub_files_count
            tree.insert(1, item)
        else:
            files_count += 1
            tree.append(item)
    return tree, directories_count, files_count


def print_tree(tree: list, decor_prefix: str = ""):
    """
    Function to print the tree from given list of directories and files

    :param tree: List of directories and files
    :param decor_prefix: Prefix needed to visualize the depth and symbols of tree
    """
    print(f"{Fore.BLUE}{tree.pop(0)}")
    for index, item in enumerate(tree, 1):
        if index == len(tree):
            print(f"{Fore.WHITE}{decor_prefix}{BRANCH_END}", end='')
            decor_plus = BRANCH_SPACE
        else:
            print(f"{Fore.WHITE}{decor_prefix}{BRANCH_RIGHT}", end='')
            decor_plus = BRANCH_LEFT

        if isinstance(item, list) and len(item) == 1:
            print(f"{Fore.BLUE}{item[0]}")
        elif isinstance(item, list):
            print_tree(item, decor_prefix + decor_plus)
        else:
            print(f"{Fore.GREEN}{item}")


def parse_arguments():
    """
    Function to parse arguments from the command line

    :return: arguments from the command line
    """
    parser = argparse.ArgumentParser(
        description="displays the directory structure as a tree with a specified depth")
    parser.add_argument("-L", "--depth", type=int, default=1,
                        help="Depth (nesting level) to display")
    parser.add_argument("directory", type=str, help="Path to the directory")

    args = parser.parse_args()
    print(type(args))
    return args


def validate_arguments(args) -> bool:
    """
    Function to validate arguments from the command line

    :param args: Arguments to validate
    :return: True if the arguments are valid
    """
    if args.depth <= 0 or args.depth >= 500:
        print(f"{Fore.RED}ERROR: Depth must be greater than 0 and less than 500")
    elif not os.path.isdir(args.directory):
        print(f"{Fore.RED}ERROR: Directory not found")
    else:
        return True


def main():
    init()
    args = parse_arguments()
    if not validate_arguments(args):
        return
    tree, directories_count, files_count = explore_directory(
        args.directory, args.depth)
    print_tree(tree)
    print(
        f"\n{Fore.WHITE}Found {directories_count} directories and {files_count} files")


if __name__ == "__main__":
    main()
