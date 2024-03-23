import argparse
import os

TAB = "     "
LINE = "│    "
MIDDLE = "├─── "
LAST = "└─── "


def print_tree(element: str, directory: str) -> None:
    if os.path.isdir(directory):
        print(element)
    elif os.path.isfile(directory):
        print(element)
    elif os.path.islink(directory):
        print(element)
    else:
        print(element)


def create_tree(indir: str, depth: int) -> list:
    tree_lst = [os.path.basename(indir)]
    if depth == 0:
        return tree_lst[0]
    try:
        indir_content = os.listdir(indir)
    except Exception:
        print('Something went wrong!')
    else:
        for item in indir_content:
            path = os.path.join(indir, item)
            if os.path.isdir(path):
                item = create_tree(path, depth - 1)
            tree_lst.append(item)

        return tree_lst


def output_tree(tree_lst: list, indir: str, prefix='') -> None:
    if len(tree_lst) == 0:
        print('Keep the depth parameter greater than 0')
        return

    # print(*tree_lst)
    elem = tree_lst.pop(0)
    print_tree(elem, indir)
    for i, item in enumerate(tree_lst):
        if i == len(tree_lst) - 1:
            prefix_add = TAB
            print(prefix + LAST, end=' ')
        else:
            prefix_add = LINE
            print(prefix + MIDDLE, end=' ')
        if type(item) is list:
            paths = os.path.join(indir, item[0])
            output_tree(item, paths, prefix + prefix_add)
        else:
            paths = os.path.join(indir, item)
            print_tree(item, paths)


def main():
    parser = argparse.ArgumentParser(description='command line')
    parser.add_argument('command', type=str, help='Command name')
    parser.add_argument('-L', type=int, help='Depth of the directory')
    parser.add_argument('indir', type=str, default='.', help='Tree stand directory')
    args = parser.parse_args()
    if args.command == 'tree':
        output_tree(create_tree(args.indir, args.L), args.indir)
    else:
        print('Unknown command')


if __name__ == '__main__':
    main()

# ЯЯЯЯ\Бомонка\Python\iu4-2k24-python\blokhin_m\task02\src\task02
