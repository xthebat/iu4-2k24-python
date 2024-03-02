import os


def collect_tree(lvl: int, path: str):
    elements = []
    lvl = lvl - 1
    array = os.listdir(path)
    for element in sorted(array):
        if os.path.isdir(os.path.join(path, element)):
            if lvl > 0:
                elements.insert(0, collect_tree(
                    lvl, os.path.join(path, element)))
            elements.insert(0, f"\033[34m{element}")

        else:
            elements.append(f"\033[32m{element}")

    return elements


def tree(arrays: list, lvl: int):
    dirs, files = 0, 0
    for element in arrays:
        if isinstance(element, list):
            lvl += 1
            count = tree(element, lvl)
            dirs += count[0]
            files += count[1]
            lvl -= 1
        else:
            if "\033[34m" in element:
                dirs += 1
            else:
                files += 1
            for i in range(lvl):
                print("    ", end='')
            print(element)

    return dirs, files


def main(lvl: int, path: str):
    collection = collect_tree(lvl, path)
    count = tree(collection, 0)
    count_str = f"\n{count[0]} directories, {count[1]} files"
    print(f"\033[0m{count_str}")


if __name__ == "__main__":
    main(3, "./")
