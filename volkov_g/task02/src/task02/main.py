import os
import colorama
from colorama import Fore
colorama.init()


def tree_dir(path: str = None, depth: int = 1, skip: int = 0, skip_stick: int = 0, list_tree: list = None) -> list:
    """
        path: str path of start
        depth: int depth of tree
        skip: int count of space, define folder nesting
        return: int count of folder,count of file, tree
        skip_stick: int need for delite past stick
    """
    list_tree = [0, 0] if list_tree is None else list_tree
    if path is None:
        path = os.getcwd()
    dir_cur = os.listdir(path)

    for dir_str in dir_cur:

        list_tree.append(skip)
        list_tree.append(dir_str)

        dir_str = os.path.join(path, dir_str)
        if os.path.isdir(dir_str):
            list_tree[0] += 1
            list_tree[-2] += 1000
            if depth > 1:
                list_tree = tree_dir(dir_str, depth-1, skip+1, skip_stick, list_tree)
        else:
            list_tree[1] += 1

    return list_tree


def tree_print(list_tree: list) -> None:

    print(f"folders: {list_tree[0]} file: {list_tree[1]}")

    print_skip = 0
    for count_drench in range(2, len(list_tree), 2):

        for check_drench in range(count_drench+2, len(list_tree), 2):

            if (list_tree[check_drench] % 1000) >= (list_tree[count_drench] % 1000):
                if (list_tree[check_drench] % 1000) == (list_tree[count_drench] % 1000):
                    print(
                        f"{Fore.RESET}{'      ' * print_skip}"
                        f"{'│     ' * (list_tree[count_drench] % 1000 - print_skip)}"
                        f"├—————{Fore.BLUE if (list_tree[count_drench]/1000) >= 1 else Fore.GREEN}"
                        f"{list_tree[count_drench + 1]}")
                    break
            else:
                print(
                    f"{Fore.RESET}{'      ' * print_skip}"
                    f"{'│     ' * (list_tree[count_drench] % 1000 - print_skip)}"
                    f"└—————{Fore.BLUE if (list_tree[count_drench]/1000) >= 1 else Fore.GREEN}"
                    f"{list_tree[count_drench + 1]}")
                break

            if check_drench == len(list_tree)-2:
                print(f"{Fore.RESET}{'      ' * print_skip}"
                      f"{'│     ' * (list_tree[count_drench] % 1000 - print_skip)}"
                      f"└—————{Fore.BLUE if (list_tree[count_drench]/1000) >= 1 else Fore.GREEN}"
                      f"{list_tree[count_drench + 1]}")
                print_skip += 1
                break

    print(f"{Fore.RESET}{'      ' * print_skip}"
          f"{'│     ' * (list_tree[len(list_tree) - 2] % 1000 - print_skip)}"
          f"└—————{Fore.BLUE if (list_tree[len(list_tree)-2]/1000) >= 1 else Fore.GREEN}"
          f"{list_tree[len(list_tree)-1]}{Fore.RESET}")


tree_print(tree_dir("test folders", 3))
print(tree_dir("test folders", 3))
