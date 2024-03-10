import os
from colorama import Fore, Style

TAB = "     "
LINE = "│    "
MIDDLE = "├─── "
LAST = "└─── "


def create_tree(directory: str, level: int) -> list[str]:
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
    try:
        os.listdir(element)
    except PermissionError:
        print(f"{Fore.RED}PERMISSION DENIED {element}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}DIRECTORY NOT FOUND {element}{Style.RESET_ALL}")


def output_tree(tree: list, directory: str, decorator: bool, number_element=None, prefix='') -> list[int]:
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

        if type(item) is list:
            path = os.path.join(directory, item[0])
            number_element = output_tree(item, path, decorator, number_element, prefix + prefix_add)
        else:
            path = os.path.join(directory, item)
            number_element = count_elements(path, number_element)
            decoration(item, path, decorator)
    return number_element


def count_elements(element: str, number_element: list[int]) -> list[int]:
    if os.path.isdir(element):
        number_element[0] = number_element[0] + 1
    elif os.path.isfile(element):
        number_element[1] = number_element[1] + 1
    return number_element


def decoration(element: str, directory: str, decorator: bool) -> None:
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
    print(f'\n{number_element[0]} directories', end=', ')
    print(f'{number_element[1]} files')
