import argparse
import os

from colorama import init, Fore, Back

from task02 import tree

init(autoreset=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tree")
    parser.add_argument("-L", "--depth", type=int, default=1, help='Tree depth')
    parser.add_argument("start_path", type=str, default=os.getcwd(), help="Path to directory")
    args = parser.parse_args()
    # args.start_path = os.path.abspath(args.start_path)
    if not os.path.isdir(args.start_path):
        print("ERROR: Inaccessible directory path")
    else:
        level_tree: int = 1
        prefix: str = ""
        calculation: list = [0, 0]
        print(Fore.BLACK + Back.LIGHTGREEN_EX + args.start_path)
        tree.print_tree(os.path.abspath(args.start_path), tree.get_tree(args.start_path, args.depth, level_tree),
                        prefix, calculation)
        print("")
        print(f"{Fore.LIGHTCYAN_EX} {calculation[0]} directories, {calculation[1]} files")
    pass
