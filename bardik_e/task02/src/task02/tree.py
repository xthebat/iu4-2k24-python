import os
from colorama import Fore, Style

# special constants for pretty output like classic tree program
PIPE = "│   "
TEE = "├───"
ELBOW = "└───"
BLANK = "    "


def run(path: str, depth: int) -> None:
	"""

	:param path: start path of the tree output
	:param depth: depth that [probably] provided as start argument
	"""

	# start condition for recursive calls
	current_depth = 0
	print(path)
	list_dir(path, current_depth, depth, "")


def list_dir(path: str, current_depth: int, start_depth: int, prefix: str) -> None:
	"""

	:param path: path to handling file or directory
	:param current_depth: current tree level
	:param start_depth: depth that [probably] provided as start argument
	:param prefix: prefix that filling recursively for pretty output
	"""

	# if depth isn't provided or current tree level less than provided maximum
	if (start_depth < 0) or (start_depth > 0 and (start_depth - current_depth)):
		try:
			# trying to fetch directory entries
			dir_items = sorted(os.listdir(path))

		except (PermissionError, FileNotFoundError):
			# if it was unsuccessfully, printing notice with red font
			print(f"{prefix}{ELBOW}{Fore.RED}PERMISSION DENIED{Style.RESET_ALL}")

		else:
			# else, iterating over directory items
			for item in dir_items:
				print(prefix, end="")
				full_path = os.path.join(path, item)

				# checking if current item last or not last in entry list,
				# printing appropriate prefix symbol
				# and setting prefix addition symbol
				if item != dir_items[-1]:
					print(TEE, end="")
					addition = PIPE
				else:
					print(ELBOW, end="")
					addition = BLANK

				# print special escape-chars for colorized output
				if os.path.isdir(full_path):
					print(Fore.BLUE, end="")
				elif os.path.islink(full_path):
					print(Fore.CYAN, end="")
				else:
					print(Fore.GREEN, end="")

				# entry name
				print(item, end="")

				# if entry is a symlink, print link's source file path
				if os.path.islink(full_path):
					print(f" -> {os.path.realpath(full_path)}", end="")

				# print special escape-char for colorized output end
				print(Style.RESET_ALL)

				# if entry is a directory, call this func recursively
				# with prefix updated with addition
				if os.path.isdir(full_path):
					list_dir(full_path, current_depth + 1, start_depth, prefix + addition)
