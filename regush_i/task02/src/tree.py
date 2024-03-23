""" A program the analogue of the tree utility """

import os
import argparse


def tree_default(directory: str, indent=0, prefix: str = "") -> list:
    """ Return a list with tree directories

    Args:
        directory (_type_): _description_
        indent (int, optional): _description_. Defaults to 0.
        prefix (str, optional): _description_. Defaults to "".

    Returns:
        list: directory tree in list
    """
    result = []
    dir_list = os.listdir(directory)

    for item in dir_list:
        path = os.path.join(directory, item)

        if item == dir_list[-1]:
            result.append(prefix + '└──' + item)
        else:
            result.append(prefix + '├──' + item)
        if os.path.isdir(path):
            if item == dir_list[-1]:
                result.extend(tree_default(path, indent + 1,  prefix + '    '))
            else:
                result.extend(tree_default(path, indent + 1,  prefix + '│   '))

    return result


def tree_level(directory: str, level=0, prefix: str = "") -> list:
    """ Return a list with tree directories with depth level

    Args:
        directory : Directory for tree
        level (int, optional): Level for tree Defaults to -1.
        prefix (str, optional): Prefix for prety output

    Returns:
        list: directory tree in list
    """
    if level == 0:
        return []

    result = []
    dir_list = os.listdir(directory)

    for item in dir_list:
        path = os.path.join(directory, item)
        if item == dir_list[-1]:
            result.append(prefix + '└──' + item)
        else:
            result.append(prefix + '├──' + item)

        if os.path.isdir(path):
            if item == dir_list[-1]:
                result.extend(tree_level(path, level - 1,  prefix + '   '))
            else:
                result.extend(tree_level(path, level - 1,  prefix + '│  '))
    return result


def tree(directory: str, level=-1) -> str:
    """ Return a string tree of directory from input directory

    Args:
        directory : Directory for tree
        level (int, optional): Level for tree Defaults to -1.

    Returns:
        str: directory tree in string 
    """
    if level == -1:
        return '\n'.join(tree_default(directory))

    return '\n'.join(tree_level(directory, level))


def main():
    """ main function for starting program """

    parser = argparse.ArgumentParser(description='Display directory tree.')
    parser.add_argument('directory', nargs='?', default='.',
                        help='Directory to display tree for (default: current directory)')
    parser.add_argument('-L', '--level',  default='-1', type=int,
                        help='Depth of the directory tree to display')

    args = parser.parse_args()

    level = args.level if args.level is not None else -1

    result = tree(args.directory, level)

    print(result)


if __name__ == '__main__':
    main()
