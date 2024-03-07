import os

def gen_tree(path: str, lvl: int):
    directory_tree = []
    for address, dirs, files in os.walk(path):
        level = address.replace(path, '').count(os.sep)
        if level < lvl:
            directory_tree.append((address, level))
    print(directory_tree)
    return directory_tree

def print_tree(directory_tree):
    for address, level in directory_tree:
        indent = '  ' * level
        print(f"{indent}|-- {os.path.basename(address)}")

# def main():
     # print_tree(gen_tree(args.path, args.lvl))

# if __name__ == "__main__":
     # parser = argp.ArgumentParser(description="Catch your path and level")
     # parser.add_argument("path", type=str, help="Path to the directory")
     # parser.add_argument("lvl", type=int, help="Nesting level")
     # args = parser.parse_args()
     # main()
     