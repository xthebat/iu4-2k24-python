import os
import sys

# Prefix components:
SPACE = '    '
BRANCH = '│   '
TEE = '├── '
LAST = '└── '

# Colors for console output
WHITE = '\033[0m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[31m'


def explore_directory(directory: str) -> list:
    directories = []
    files = []

    try:
        items = os.listdir(directory)
    except PermissionError:
        print(f"{RED} ERROR: Нет доступа к директории или поддиректории")
        return [], []

    for item in items:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            directories.append(item)
        else:
            files.append(item)

    return directories, files


def print_tree(directory: str, max_depth: int = 999, indent: str = '', depth: int = 0, is_root: bool = True) -> int:
    if is_root:
        print(f'{BLUE}{directory}')  # Выводим корневую директорию
    directories, files = explore_directory(directory)
    directories_count = 0
    files_count = len(files)

    for i, item in enumerate(directories + files):
        is_last = i == len(directories + files) - 1
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(f'{WHITE}{indent}{(LAST if is_last else TEE)}{BLUE}{item}')
            if os.path.isdir(item_path) and depth < max_depth:
                sub_directories_count, sub_files_count = print_tree(
                    item_path, max_depth, f'{indent}{(SPACE if is_last else BRANCH)}', depth + 1, False)
                directories_count += sub_directories_count
                files_count += sub_files_count
            directories_count += 1
        else:
            print(f'{WHITE}{indent}{(LAST if is_last else TEE)}{GREEN}{item}')

    if depth == 0:
        print(f'{WHITE}', end='')
        print(f'\nВсего {directories_count} директорий, {files_count} файлов')

    return directories_count, files_count


if __name__ == "__main__":
    if len(sys.argv) > 2:
        start_directory = sys.argv[2]
        try:
            max_depth = int(sys.argv[1]) - 1
            if max_depth < 0:
                print(f"{RED} ERROR: Уровень вложенности должен быть больше 0")
            elif not os.path.isdir(start_directory):
                print(f"{RED} ERROR: Нет такой директории")
            else:
                print_tree(start_directory, max_depth)
        except:
            print(
                f"{RED} ERROR: Уровень вложенности должен быть целым не отрицательным числом и больше 0")
    else:
        print(
            f"{RED} ERROR: Необходимо ввести два аргумента: уровень вложенности и путь")
