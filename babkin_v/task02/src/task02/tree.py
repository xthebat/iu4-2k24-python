import os


def print_level(name, current_level):
    print("|  " * (current_level - 1) + "|--" + f"{name}")


def print_tree(level: int, path: str, current_level=0):
    list1 = os.listdir(os.path.normcase(path))
    current_level += 1
    for name in list1:
        new_path = os.path.join(path, name)
        print_level(name, current_level)
        if current_level < level and os.path.isdir(new_path):
            print_tree(level, new_path, current_level)


print_tree(3, 'C:/progani/repos/iu4/babkin_v')
