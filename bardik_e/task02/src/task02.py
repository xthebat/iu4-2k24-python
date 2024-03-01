import argparse
import os
from task02 import tree

if __name__ == "__main__":

	# initializing argument parser object and adding needed params
	parser = argparse.ArgumentParser(description="Tree - recursive ls.")
	parser.add_argument("path", type=str, default=os.getcwd(),
		nargs=1, help="Path to directory that will be recursively scanned.")
	parser.add_argument("-d", "--depth", type=int, default=-1,
		nargs=1, help="Maximum depth of tree.")
	args = parser.parse_args()

	# if presented string is not a valid path, raise an error
	if not os.path.isdir(args.path[0]):
		parser.error("provided string is not a valid path")

	# if tree depth is not provided, args.depth will be int and == -1
	# if tree depth is provided, args.depth will be list with 1 item
	# call start function with this params
	tree.run(args.path[0], int(args.depth[0] if isinstance(args.depth, list) else args.depth))
