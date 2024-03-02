from os import listdir
from os.path import isdir

def tree(lvl:int, path:str):
    elements = []
    lvl = lvl - 1
    arr = listdir(path)
    for e in sorted(arr):
        if isdir(f"{path}/{e}"):
            if lvl > 0:
                elements.insert(0, tree(lvl, f"{path}/{e}"))
            elements.insert(0, f"\033[34m{e}")
        else:
            elements.append(f"\033[32m{e}")

    return elements 

def print_result(arrays, lvl):
    dirs, files = 0, 0
    for e in arrays:
        if isinstance(e, list):
            lvl += 1
            count = print_result(e, lvl)
            dirs += count[0]
            files += count[1]
            lvl -= 1
        else:
            if "\033[34m" in e:
                dirs += 1
            else:
                files += 1
            print(lvl * "   " + e)

    return dirs, files

def main(lvl:int, path:str):
    mass = tree(lvl, path)
    count = print_result(mass, 0)
    print("\033[0m{}".format(f"\n{count[0]} directories, {count[1]} files"))

if __name__ == "__main__":
    main(3,"./")