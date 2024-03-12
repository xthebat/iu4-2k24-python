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
            print(element)
        elif os.path.isfile(directory):
            print(element)
        elif os.path.islink(directory):
            print(element)
        else:
            print(element)
    else:
        print(element)


# Creates a list of directories and files in them
def create_tree(indir: str, depth: int) -> list:
    tree_lst = [os.path.basename(indir)]
    if depth == 0:
        return tree_lst[0]
    # Handler of errors
    try:
        directory_content = os.listdir(indir)
    except PermissionError:
        print(f"PERMISSION DENIED {indir}")
        return tree_lst[0]
    except FileNotFoundError:
        print(f"DIRECTORY NOT FOUND {indir}")
        return []
    # Deepening into the depths of directories
    for item in directory_content:
        path = os.path.join(indir, item)
        if os.path.isdir(path):
            item = create_tree(path, depth - 1)
        tree_lst.append(item)

    return tree_lst


# Displaying a list of directories and files in the "tree" format
def output_tree(tree_lst: list, indir: str, prefix='') -> str:
    decorate = ''
    if len(tree_lst) == 0:
        return decorate
    element = tree_lst.pop(0)
    decoration(element, indir, decorate)
    # Display prefix
    for i, item in enumerate(tree_lst):
        if i == len(tree_lst) - 1:
            prefix_add = TAB
            print(prefix + LAST, end='')
        else:
            prefix_add = LINE
            print(prefix + MIDDLE, end='')
        # Go down into the depths and output structure
        if type(item) is list:
            path = os.path.join(indir, item[0])
            output_tree(item, path, prefix + prefix_add)
        else:
            path = os.path.join(indir, item)
            decoration(item, path, decorate)
