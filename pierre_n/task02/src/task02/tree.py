import os
from colorama import init, Fore

init(autoreset=True)

def get_directory_tree(directory):
    tree = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            tree.append((item_path, True))
            tree.extend(get_directory_tree(item_path))
        else:
            tree.append((item_path, False))
    return tree

def display_tree(tree, indent='', max_depth=None):
    for i, (item_path, is_directory) in enumerate(tree):
        if max_depth is not None and indent.count('│') >= max_depth:
            return
        if i == len(tree) - 1:
            display_tree_prefix = '└── '
            sub_tree_prefix = '    '
        else:
            display_tree_prefix = '├── '
            sub_tree_prefix = '│   '
        print(indent + display_tree_prefix + (Fore.BLUE if is_directory else Fore.GREEN) + os.path.basename(item_path))
        if is_directory:
            sub_indent = indent + sub_tree_prefix
            sub_tree = get_directory_tree(item_path)
            display_tree(sub_tree, sub_indent, max_depth)

