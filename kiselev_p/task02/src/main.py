from tree import Tree
from argparse import ArgumentParser

def parseArg():
    """Parses the arguments passed on the command line
    """        

    parser = ArgumentParser(description="Build tree of filesystem")

    parser.add_argument("path",type=str, help="start directory")
    parser.add_argument("-d", "--depth", dest="depth", default=None, type=int,
                            help="tree display depth [default: %(default)s]")
    parser.add_argument("-s", "--sort", dest="sort", default=None, type=str,
                            choices=["asc", "desc"],
                            help="sorting asc/desc [default: %(default)s]")
    return parser.parse_args()

def main():
    arg = parseArg()
    tree = Tree()
    tree.build(arg.path, arg.depth, arg.sort)

if __name__ == "__main__":
    main()