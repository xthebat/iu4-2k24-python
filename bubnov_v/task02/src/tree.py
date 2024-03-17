import os
from colorama import Fore, Style

TAB = "     "
LINE = "│    "
MIDDLE = "├─── "
LAST = "└─── "


def create_tree(directory: str, level: int) -> list[str]:
    """
    Recursively generates a directory tree structure up to the specified level.

    Args:
        directory (str): The path to the directory.
        level (int): The depth of the directory tree to generate.

    Returns:
        list[str]: A list representing the directory tree structure.
    """
    tree_lst = [os.path.basename(directory)]
    if level == 0:
        return tree_lst[0]

    check_element(directory)
    try:
        os.listdir(directory)
    except PermissionError:
        return tree_lst[0]
    except FileNotFoundError:
        return []

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            item = create_tree(path, level - 1)
        tree_lst.append(item)
    return tree_lst


def check_element(element: str) -> None:
    """
    Checks if the specified element exists and display an error message if it doesn't or if permission is denied.

    Args:
        element (str): The path to the directory or file to check.
    """
    try:
        os.listdir(element)
    except PermissionError:
        print(f"{Fore.RED}PERMISSION DENIED {element}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}DIRECTORY NOT FOUND {element}{Style.RESET_ALL}")


def output_tree(tree: list, directory: str, decorator: bool, number_element=None, prefix='') -> list[int]:
    """
    Recursively outputs the directory tree structure with optional decorations.

    Args:
        tree (list): The directory tree structure to output.
        directory (str): The path to the current directory.
        decorator (bool): Whether to decorate directory and file names.
        number_element (list[int], optional): A list containing the count of directories and files. Defaults to None.
        prefix (str, optional): The prefix for indentation. Defaults to ''.

    Returns:
        list[int]: A list containing the count of directories and files.
    """
    if number_element is None:
        number_element = [0, 0]
    if len(tree) == 0:
        return number_element

    element = tree.pop(0)
    number_element = count_elements(directory, number_element)
    decoration(element, directory, decorator)

    for i, item in enumerate(tree):
        if i == len(tree) - 1:
            prefix_add = TAB
            print(prefix + LAST, end='')
        else:
            prefix_add = LINE
            print(prefix + MIDDLE, end='')

        if isinstance(item, list):
            path = os.path.join(directory, item[0])
            number_element = output_tree(item, path, decorator, number_element, prefix + prefix_add)
        else:
            path = os.path.join(directory, item)
            number_element = count_elements(path, number_element)
            decoration(item, path, decorator)
    return number_element


def count_elements(element: str, number_element: list[int]) -> list[int]:
    """
    Counts the number of directories and files.

    Args:
        element (str): The path to the directory or file.
        number_element (list[int]): A list containing the count of directories and files.

    Returns:
        list[int]: A list containing the updated count of directories and files.
    """
    if os.path.isdir(element):
        number_element[0] = number_element[0] + 1
    elif os.path.isfile(element):
        number_element[1] = number_element[1] + 1
    return number_element


def decoration(element: str, directory: str, decorator: bool) -> None:
    """
    Decorates directory and file names if specified.

    Args:
        element (str): The name of the directory or file.
        directory (str): The path to the current directory.
        decorator (bool): Whether to decorate directory and file names.
    """
    if decorator:
        if os.path.isdir(directory):
            print(Fore.BLUE + element + Style.RESET_ALL)
        elif os.path.isfile(directory):
            print(Fore.GREEN + element + Style.RESET_ALL)
        else:
            print(element)
    else:
        print(element)


def total_number_element(number_element: list[int]) -> None:
    """
    Display the total count of directories and files.

    Args:
        number_element (list[int]): A list containing the count of directories and files.
    """
    print(f'\n{number_element[0]} directories', end=', ')
    print(f'{number_element[1]} files')
