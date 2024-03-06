import os
import argparse
from colorama import Fore, Style
from pathlib import Path

CROWBAR = '└──'
T_LEFT = '├──'
LINE = '│    '
BLANK = '    '

directories_count = 0
files_count = 0


def generate_tree(path: Path, depth=1, prefix="") -> str:
    result = ""
    items_list = os.listdir(path)
    for item in items_list:
        is_last = True if item == items_list[-1] else False
        item_path = os.path.join(path, item)
        result = f"{result}{prefix}{generate_string(item_path, is_last, item)}\n\r"
        if depth > 1:
            if os.path.isdir(item_path):
                addon = generate_tree(item_path, depth - 1, f"{prefix}{BLANK if is_last else LINE}")
                result = f"{result}{addon}"
    return result


def generate_string(item_path: Path, is_last: bool, name: str):
    if os.path.isdir(item_path):
        style = Fore.BLUE
        global directories_count
        directories_count += 1
    elif os.path.islink(item_path):
        style = Fore.CYAN
    elif os.path.isfile(item_path):
        style = Fore.GREEN
        global files_count
        files_count += 1
    else:
        style = Fore.RED
    string = f"{CROWBAR if is_last else T_LEFT} {style}{name}{Style.RESET_ALL}"
    return string


def range_type(astr: str, min=1, max=20) -> int:
    value = int(astr)
    if min <= value <= max:
        return value
    else:
        raise argparse.ArgumentTypeError('value not in range %s-%s' % (min, max))


def dir_type(path: str):
    if os.path.isdir(os.path.normcase(path)):
        return path
    else:
        raise argparse.ArgumentTypeError(f"path ({path}) is not a directory")


if __name__ == '__main__':
    # I need to invoke tree.py with 2 parameters: 'level' and 'path'
    # Best if I can print errors in case of incorrect input like:
    # too little or too much args, level not a int OR  level<1, path not a str OR str not a real path to dir
    # Best if I can describe unit test for it
    # Additionally argparse lib can generate help and usage messages, would be useful and nice
    parser = argparse.ArgumentParser()
    parser.add_argument("level", help="depth of tree",
                        # type=range_type,
                        type=int,
                        choices=range(1, 20), nargs='?', default=20,
                        metavar="level[0-20]")
    parser.add_argument("path", nargs='?', default='.', help="path to directory"
                        # , type=dir_type
                        )
    args = parser.parse_args()

    print(f"level: {args.level}")
    print(f"path: {args.path}")
    print(f"{Fore.BLUE}{args.path}{Style.RESET_ALL}")
    print(generate_tree(args.path, args.level).rstrip())
    print(f"directories_count: {directories_count}")
    print(f"files_count: {files_count}")
