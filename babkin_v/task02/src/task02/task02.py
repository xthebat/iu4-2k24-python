import os
import argparse

from colorama import Fore, Style
from pathlib import Path

CROWBAR = '└──'
T_LEFT = '├──'
LINE = '│    '
BLANK = '     '


def generate_tree(path: Path, counter: dict, depth=1, prefix="" ) -> str:
    result = ""
    for item in sorted(os.listdir(path)): # for item in sorted(os.listdir(path))
        is_last = item == sorted(os.listdir(path))[-1]  # is_last = True if item == items_list[-1] else False
        item_path = os.path.join(path, item)
        is_dir = os.path.isdir(item_path)
        name_with_color = generate_string(is_dir, is_last, item, counter)
        result = f"{result}{prefix}{name_with_color}\n\r"
        if depth > 1:
            if os.path.isdir(item_path):
                extender = f"{prefix}{BLANK if is_last else LINE}"
                addon = generate_tree(item_path, counter, depth - 1, extender)
                result = f"{result}{addon}"
    return result


def generate_string(is_dir, is_last: bool, name: str, counter: dict) -> str:
    if is_dir:
        style = Fore.BLUE
        counter['directories'] += 1
    else:
        style = Fore.GREEN
        counter['files'] += 1

    string = f"{CROWBAR if is_last else T_LEFT} {style}{name}{Style.RESET_ALL}"
    return string


def range_type(astr: str, min=1, max=30) -> int:
    value = int(astr)
    if min <= value <= max:
        return value
    else:
        raise argparse.ArgumentTypeError('value not in range %s-%s' % (min, max))


def dir_type(path: str):
    if os.path.isdir(os.path.normcase(path)):
        return path
    raise argparse.ArgumentTypeError(f"path ({path}) is not a directory")


def main():
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
    counter = {
        'directories': 0,
        'files': 0
    }
    print(f"{Fore.BLUE}{os.path.abspath(args.path)}{Style.RESET_ALL}")
    print(generate_tree(args.path, counter,  args.level))
    print(f"directories: {counter['directories']}")
    print(f"files: {counter['files']}")


if __name__ == '__main__':
    main()
