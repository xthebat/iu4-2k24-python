import os
import sys

directories_count = 0
files_count = 0

# Prefix components:
space = '    '
branch = '│   '
tee = '├── '
last = '└── '

# Colors for console output
white = '\033[0m'
blue = '\033[94m'
green = '\033[92m'
red = '\033[31m'


def tree(directory: str, max_depth: int = 0, depth: int = 0, indent: str = ''):
    global directories_count, files_count
    directories = []
    files = []

    if depth == 0:
        print(f"{blue}{directory}")
    elif depth > max_depth:
        return

    try:
        items = os.listdir(directory)
    except PermissionError:
        return

    for item in sorted(items):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            directories_count += 1
            directories.append(item)
        else:
            files_count += 1
            files.append(item)

    for i, item in enumerate(directories):
        path = os.path.join(directory, item)
        if i == len(directories) - 1 and not files:
            print(f"{white}{indent}{last}{blue}{item}")
            tree(path, max_depth, depth + 1, f"{indent}{space}")
        else:
            print(f"{white}{indent}{tee}{blue}{item}")
            tree(path, max_depth, depth + 1, f"{indent}{branch}")

    for i, item in enumerate(files):
        path = os.path.join(directory, item)
        if i == len(files) - 1:
            print(f"{white}{indent}{last}{green}{item}")
        else:
            print(f"{white}{indent}{tee}{green}{item}")

    if depth == 0:
        print(white, end='')
        print(f"\nВсего {directories_count} директорий, {files_count} файлов")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        my_path = sys.argv[2]
        try:
            lvl = int(sys.argv[1]) - 1
            if lvl < 0:
                print(f"{red} ERROR: Уровень вложенности должен быть больше 0")
            elif not os.path.isdir(my_path):
                print(f"{red} ERROR: Нет такой директории")
            else:
                tree(my_path, lvl)
        except:
            print(
                f"{red} ERROR: Уровень вложенности должен быть целым не отрицательным числом и больше 0")
    else:
        print(
            f"{red} ERROR: Необходимо ввести два аргумента: уровень вложенности и путь")
