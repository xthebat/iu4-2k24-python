import os

# Symbols of tree in ASCII transformed to string
down_right = chr(9568)
down = chr(9553)
right = chr(9562)
flat = chr(9552)


# Function to collect directories and files to a list
def collect_tree(lvl: int, path: str) -> list:
    elements = []
    lvl -= 1
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


# Function to print and count directories and files
def tree(arrays: list, lvl: int) -> int:
    dirs, files = 0, 0

    for element in arrays:
        if isinstance(element, list):
            count = tree(element, lvl + 1)
            dirs += count[0]
            files += count[1]

        else:
            if lvl > 0:
                print(f"\033[0m{down}", end='')
                for i in range(lvl):
                    print("   ", end='')
                    if i == lvl-1:
                        if element == arrays[-1]:
                            print(f"\033[0m{right}", end='')
                        else:
                            print(f"\033[0m{down_right}", end='')
                    else:
                        print(f"\033[0m{down}", end='')
            else:
                if element == arrays[-1]:
                    print(f"\033[0m{right}", end='')
                else:
                    print(f"\033[0m{down_right}", end='')

            if "\033[34m" in element:
                dirs += 1
            else:
                files += 1
            for i in range(2):
                print(f"\033[0m{flat}", end='')
            print(f" {element}")

    return dirs, files


def main(lvl: int, path: str):
    collection = collect_tree(lvl, path)

    print(f"\033[34m{path}")
    count = tree(collection, 0)

    count_str = f"\n{count[0]} directories, {count[1]} files"
    print(f"\033[0m{count_str}")


if __name__ == "__main__":
    main(3, "./Nurumov_r")
