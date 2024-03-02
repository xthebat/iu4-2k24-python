import os
import argparse


def generate_tree(directory, req_depth, current_depth = 1, decor_prefix=""):
    if current_depth > req_depth:
        return
    # print directory name
    cur_dir = (decor_prefix + os.path.basename(directory))
    if cur_dir == "":           # user used a relative path
        print(os.path.basename(os.path.abspath(directory)))
    else:                       # user used an absolute path
        print(cur_dir)
    # print the list of the items contained in directory
    list_of_items = os.listdir(directory)
    num_of_items = len(list_of_items)
    i = 0                       # index of the current item
    for item in list_of_items:
        i += 1
        if i == num_of_items:   # end item of the branch
            print(decor_prefix + "\\-- " + item)
        else:
            print(decor_prefix + "|-- " + item)
        # check if current item is directory
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            if i == num_of_items:
                new_decor_prefix = decor_prefix + "    "
            else:
                new_decor_prefix = decor_prefix + "|   "
            # recursive call of the generate_tree() function
            generate_tree(item_path, req_depth,
                          current_depth + 1, new_decor_prefix)

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(
        description="displays the directory structure as a tree with a specified depth")
    parser.add_argument("-L", "--depth", type=int, default=1,
                        help="Depth (nesting level) to display")
    parser.add_argument("directory", type=str, help="Path to the directory")

    args = parser.parse_args()
    generate_tree(args.directory, args.depth)
