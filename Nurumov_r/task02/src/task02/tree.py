import os

# Symbols of tree in ASCII transformed to string
down_right = chr(9568)
down = chr(9553)
right = chr(9562)
flat = chr(9552)

# Colors for console output
white = "\033[0m"
blue = "\033[34m"
green = "\033[32m"


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
            elements.insert(0, f"{blue}{element}")

        else:
            elements.append(f"{green}{element}")

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
                print(f"{white}{down}", end='')
                for i in range(lvl):
                    print("   ", end='')
                    if i == lvl-1:
                        if element == arrays[-1]:
                            print(f"{white}{right}", end='')
                        else:
                            print(f"{white}{down_right}", end='')
                    else:
                        print(f"{white}{down}", end='')
            else:
                if element == arrays[-1]:
                    print(f"{white}{right}", end='')
                else:
                    print(f"{white}{down_right}", end='')

            if "{blue}" in element:
                dirs += 1
            else:
                files += 1
            for i in range(2):
                print(f"{white}{flat}", end='')
            print(f" {element}")

    return dirs, files


def main(lvl: int, path: str):
    collection = collect_tree(lvl, path)

    print(f"{blue}{path}")
    count = tree(collection, 0)

    count_str = f"\n{count[0]} directories, {count[1]} files"
    print(f"{white}{count_str}")


if __name__ == "__main__":
    main(3, "./Nurumov_r")
