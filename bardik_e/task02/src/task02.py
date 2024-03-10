import argparse
import os
import sys

from task02 import tree

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Tree - recursive ls.")
	parser.add_argument("path", type=str, default=os.getcwd(),
		nargs=1, help="Path to directory that will be recursively scanned.")
	parser.add_argument("-d", "--depth", type=int, default=-1,
		nargs=1, help="Maximum depth of tree.")
	args = parser.parse_args()
	path = args.path[0]

	if not os.path.isdir(path):
		parser.error("provided string is not a valid path")

	tree.run(path, int(args.depth[0] if isinstance(args.depth, list) else args.depth), sys.stdout)
