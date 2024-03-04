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
			print_entry("PERMISSION DENIED", "", prefix, True)

		else:
			# else, iterating over directory items
			for item in dir_items:
				full_path = os.path.join(path, item)
				print_entry(item, path, prefix, item == dir_items[-1])
				addition = PIPE if item != dir_items[-1] else BLANK

				if os.path.isdir(full_path):
					list_dir(full_path, current_depth + 1, start_depth, prefix + addition)


def print_entry(name: str, path_prefix: str, prefix: str, is_last: bool) -> None:
	"""

	:param name: name of object in parent directory
	:param path_prefix: full path to parent directory
	:param prefix: print prefix
	:param is_last: flag, that set to true when object is last in parent directory
	"""
	full_path = os.path.join(path_prefix, name)

	print(f"{prefix}{ELBOW if is_last else TEE}", end="")
	print(f"{get_output_color(full_path)}{name}", end="")

	if os.path.islink(full_path):
		print(f" -> {os.path.realpath(full_path)}", end="")

	print(Style.RESET_ALL)


def get_output_color(path: str) -> str:
	"""

	:param path: path to colorizing object
	:return: ANSI-code for colorized output
	"""
	if os.path.isdir(path):
		return Fore.BLUE
	elif os.path.islink(path):
		return Fore.CYAN
	elif os.path.isfile(path):
		return Fore.GREEN
	else:
		return Fore.RED
