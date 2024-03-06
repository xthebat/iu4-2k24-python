"""Module print directory tree."""

from pathlib import Path
import os
import sys
import argparse


SPACE     =  '    '
BRANCH    = '│   '
T         = '├── '
LAST      = '└── '


def tree(path_name: Path, current_level: int, lvl_mod: bool, prefix: str='') :
    """Find and print path"""  
    contents = list(path_name.iterdir())
    pointers = [T] * (len(contents) - 1) + [LAST]
    for pointer, path in zip(pointers, contents):
        if(( current_level == 0) and lvl_mod is True):
            return 0
        print(prefix + pointer + path.name)
        current_level_nxt = current_level
        if path.is_dir(): # extend the prefix and recurse:
            if(( current_level_nxt == 0) and lvl_mod is True):
                return 0
            current_level_nxt -= 1
            extension = BRANCH if pointer == T else SPACE
            tree(path, current_level=current_level_nxt, prefix=prefix+extension, lvl_mod=lvl_mod)




def main():
    """Arg parce and program start"""
    parser = argparse.ArgumentParser(description='PCAP reader')
    parser.add_argument('-L', metavar='<depth level>', default= 0,
                        help=' setting depth level. if 0 => print all levels')
    parser.add_argument('-p', metavar='<dir path>', help=' setting start path')

    args = parser.parse_args()
    path_name = args.p

    if not os.path.isdir(path_name):
        print('"{}" does not exist'.format(path_name), file=sys.stderr)
        sys.exit(-1)
    path = Path(args.p)
    lvl_mod = int(args.L) != 0
    tree(path, current_level=int(args.L), lvl_mod = lvl_mod)

if __name__ == "__main__":
    main()
