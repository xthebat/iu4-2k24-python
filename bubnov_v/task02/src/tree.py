import os
from colorama import Fore, Style

TAB = "     "
LINE = "│    "
MIDDLE = "├─── "
LAST = "└─── "


# Colors the element when output, depending on its type
def decoration(element: str, directory: str, decorate: str) -> None:
    if not decorate:
        if os.path.isdir(directory):
            print(Fore.BLUE + element + Style.RESET_ALL)
        elif os.path.isfile(directory):
            print(Fore.GREEN + element + Style.RESET_ALL)
        elif os.path.islink(directory):
            print(Fore.LIGHTCYAN_EX + element + Style.RESET_ALL)
        else:
            print(element)
    else:
        print(element)


# Creates a list of directories and files in them
def create_tree(directory: str, level: int) -> list:
    tree_lst = [os.path.basename(directory)]
    if level == 0:
        return tree_lst[0]
    # Handler of errors
    try:
        directory_content = os.listdir(directory)
    except PermissionError:
        print(f"{Fore.RED}PERMISSION DENIED {directory}{Style.RESET_ALL}")
        return tree_lst[0]
    except FileNotFoundError:
        print(f"{Fore.RED}DIRECTORY NOT FOUND {directory}{Style.RESET_ALL}")
        return []
    # Deepening into the depths of directories
    for item in directory_content:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            item = create_tree(path, level - 1)
        tree_lst.append(item)

    return tree_lst


# Displaying a list of directories and files in the "tree" format
def output_tree(tree: list, directory: str, prefix='', decorate='') -> None:
    if len(tree) == 0:
        return
    element = tree.pop(0)
    decoration(element, directory, decorate)
    # Display prefix
    for i, item in enumerate(tree):
        if i == len(tree) - 1:
            prefix_add = TAB
            print(prefix + LAST, end='')
        else:
            prefix_add = LINE
            print(prefix + MIDDLE, end='')
        # Go down into the depths and output structure
        if type(item) is list:
            path = os.path.join(directory, item[0])
            output_tree(item, path, prefix + prefix_add, decorate)
        else:
            path = os.path.join(directory, item)
            decoration(item, path, decorate)
