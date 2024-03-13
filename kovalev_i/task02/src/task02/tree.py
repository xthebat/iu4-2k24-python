import os

from colorama import init, Fore, Back

init(autoreset=True)

BRANCH = Fore.BLUE + " │   "
CROSS = Fore.BLUE + " ├── "
PASS = Fore.BLUE + "     "
BRANCH_END = Fore.BLUE + " └── "


def get_tree(path: str, depth: int, level_tree: int) -> list:
    tree: list = []
    essences = os.listdir(path)

    for essence in essences:
        if essence.startswith('.'):
            continue
        # print(os.path.abspath(essence))
        tree.append(essence)
        if os.path.isdir(os.path.join(path, essence)):
            if level_tree < depth:
                level_tree += 1
                tree.append(get_tree(os.path.join(path, essence), depth, level_tree))
                level_tree -= 1
    return tree
    pass


def print_tree(path: str, tree: list, prefix: str, calculation: list) -> None:
    # print(f"{tree}///{len(tree)}")
    for counter in range(len(tree)):
        flag_end: bool = False
        if isinstance(tree[counter], list):
            old_prefix: str = prefix
            tmp: list = tree[counter]
            if counter != (len(tree) - 1):
                prefix += BRANCH
            else:
                prefix += PASS
            print_tree(os.path.join(path, tree[counter - 1]), tmp, prefix, calculation)
            prefix = old_prefix
        else:
            if counter == (len(tree) - 1) or (isinstance(tree[counter + 1], list) and (counter == (len(tree) - 2))):
                flag_end = True
            if os.path.isfile(os.path.join(path, tree[counter])):
                calculation[1] += 1
            if os.path.isdir(os.path.join(path, tree[counter])):
                print(prefix + BRANCH_END + Fore.BLACK + Back.LIGHTGREEN_EX + tree[counter]) if flag_end else print(
                    prefix + CROSS + Fore.BLACK + Back.LIGHTGREEN_EX + tree[counter])
                calculation[0] += 1
            elif tree[counter].endswith(".lnk"):
                link: str = os.path.realpath(os.path.join(path, tree[counter]))
                print(prefix + BRANCH_END + Fore.RED + tree[
                    counter] + " -> " + Fore.WHITE + link) if flag_end else print(
                    prefix + CROSS + Fore.RED + tree[counter] + " -> " + Fore.WHITE + link)
            elif tree[counter].endswith(".zip"):
                print(prefix + BRANCH_END + Fore.YELLOW + tree[counter]) if flag_end else print(
                    prefix + CROSS + Fore.YELLOW + tree[counter])
            elif tree[counter].endswith(".txt"):
                print(prefix + BRANCH_END + Fore.MAGENTA + tree[counter]) if flag_end else print(
                    prefix + CROSS + Fore.MAGENTA + tree[counter])
            elif tree[counter].endswith(".exe"):
                print(prefix + BRANCH_END + Fore.LIGHTWHITE_EX + tree[counter]) if flag_end else print(
                    prefix + CROSS + Fore.LIGHTWHITE_EX + tree[counter])
            elif tree[counter].endswith((".docx", ".DOCX", ".doc")):
                print(prefix + BRANCH_END + Fore.LIGHTWHITE_EX + Back.LIGHTBLUE_EX + tree[
                    counter]) if flag_end else print(
                    prefix + CROSS + Fore.LIGHTWHITE_EX + Back.LIGHTBLUE_EX + tree[counter])
            elif tree[counter].endswith("pdf"):
                print(prefix + BRANCH_END + Fore.LIGHTWHITE_EX + Back.LIGHTRED_EX + tree[
                    counter]) if flag_end else print(
                    prefix + CROSS + Fore.LIGHTWHITE_EX + Back.LIGHTRED_EX + tree[counter])
            elif tree[counter].endswith("xlsx"):
                print(prefix + BRANCH_END + Fore.LIGHTWHITE_EX + Back.LIGHTGREEN_EX + tree[
                    counter]) if flag_end else print(
                    prefix + CROSS + Fore.LIGHTWHITE_EX + Back.LIGHTGREEN_EX + tree[counter])
            elif tree[counter].endswith(".py"):
                print(prefix + BRANCH_END + Fore.CYAN + tree[counter]) if flag_end else print(
                    prefix + CROSS + Fore.CYAN + tree[counter])
            else:
                print(prefix + BRANCH_END + Fore.GREEN + tree[counter]) if flag_end else print(
                    prefix + CROSS + Fore.GREEN + tree[counter])
    pass
