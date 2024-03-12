import os

from colorama import init, Fore

# work on Windows
init(autoreset=True)


def find_dir_and_files(start_path: str, max_level: int) -> tuple[list[str], int, int]:
    ans = []
    number_of_directories = 0
    number_of_files = 0
    for address, dirs, files in os.walk(start_path):
        level = address.replace(start_path, '').count(os.sep)
        if level < max_level:
            indent = '-' * 4 * level
            ans.append(Fore.BLUE + f"|{indent}{os.path.basename(address)}/")
            number_of_directories += 1
            sub_indent = '-' * 4 * (level + 1)
            for f in files:
                ans.append(Fore.GREEN + f"|{sub_indent}{f}")
                number_of_files += 1
    return ans, number_of_directories, number_of_files


def print_tree(start_path: str, max_level: int):
    ans, number_of_directories, number_of_files = find_dir_and_files(start_path, max_level)
    for f in ans:
        print(f)
    print(f"{number_of_directories} directories, {number_of_files} files")
