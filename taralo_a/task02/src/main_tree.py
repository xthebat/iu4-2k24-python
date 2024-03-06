"""Module print directory tree."""

from pathlib import Path
import os
import sys
import argparse
from enum import Enum

class TreeSymbols(Enum):
    """Class with symbols for tree printing"""
    SPACE     = '    '
    BRANCH    = '│   '
    T         = '├── '
    LAST      = '└── '


def tree(path_name: Path, level: int, lvl_mod: bool, result: list=[], prefix: str='') -> list:
    """
    Dirs searching and create list
    
    path_name: path where tree must start
    level: current or max level of depth
    lvl_mod: lvl set by user or not
    result: result list for recursion (in main call should be empty)
    prefix: symbol prefix for recursion (in main call should be empty)
    """
    path_list = list(path_name.iterdir())
    symbols = [TreeSymbols.T.value] * (len(path_list) - 1) + [TreeSymbols.LAST.value]

    for symbol, path in zip(symbols, path_list):
        if level == 0 and lvl_mod is True:
            return

        result.append(prefix + symbol + path.name)

        current_level_nxt = level

        if path.is_dir():
            if current_level_nxt == 0 and lvl_mod is True:
                return

            current_level_nxt -= 1

            if symbol == TreeSymbols.T.value :
                extension_symbol = TreeSymbols.BRANCH.value 
            else :
                extension_symbol = TreeSymbols.SPACE.value

            tree(path, level=current_level_nxt, prefix=prefix+extension_symbol, lvl_mod=lvl_mod, result=result)
    return result


def print_tree(tree_lst : list) -> None:
    """"
    
    Printing tree from list
    
    tree_lst: list with dirs for printing
    """
    print('\n'.join(tree_lst))



def main():
    """Arg parce and start of program"""
    parser = argparse.ArgumentParser(description='Dir tree printing')
    parser.add_argument('-L', metavar='<depth level>', default= -1,
                        help=' setting depth level. if 0 => print all levels')
    parser.add_argument('directory', nargs='?', default='.', 
                       help='Directory to display tree for (default: current directory)')
    args = parser.parse_args()
    path_name = args.directory

    if not os.path.isdir(path_name):
        print('"{}" does not exist'.format(path_name), file=sys.stderr)
        sys.exit(-1)

    path = Path(path_name)
    lvl_mod = int(args.L) >= 0

    print_tree(tree(path, level=int(args.L), lvl_mod = lvl_mod))

if __name__ == "__main__":
    main()
