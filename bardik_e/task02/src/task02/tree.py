import os
from colorama import Fore, Style

# special constants for pretty output like classic tree program
PIPE = "│   "
TEE = "├───"
ELBOW = "└───"
BLANK = "    "


def run(path: str, depth: int, output_stream):
	"""
	:param path: start path of the tree output
	:param depth: depth that [probably] provided as start argument
	:param output_stream: file descriptor or stream object for output
	"""

	# start condition for recursive calls
	current_depth = 0

	dir_structure = create_tree(path, current_depth, depth)

	print(path, file=output_stream)
	print_tree(dir_structure[1:], "", output_stream)

	dirs_count, files_count, links_count = count_entries(dir_structure)
	print(f"\n{dirs_count} directories, {files_count} files, {links_count} links", file=output_stream)


def create_tree(path: str, current_depth: int, start_depth: int) -> list[str | list[str] | list[str, list]]:
	"""
	:param path: path to handling file or directory
	:param current_depth: current tree level
	:param start_depth: depth that [probably] provided as start argument
	"""

	result = [path]

	# if depth isn't provided or current tree level less than provided maximum
	if (start_depth < 0) or (start_depth > 0 and (start_depth - current_depth)):
		try:
			# trying to fetch directory entries
			dir_items = sorted(os.listdir(path))

		except (PermissionError, FileNotFoundError):
			# if it was unsuccessfully, printing notice with red font
			result.append([path, "PERMISSION DENIED"])

		else:
			# else, iterating over directory items
			for item in dir_items:
				full_path = os.path.join(path, item)

				if os.path.isdir(full_path):
					result.append(create_tree(full_path, current_depth + 1, start_depth))
				else:
					result.append(full_path)

	return result


def count_entries(structure: list) -> tuple[int, int, int]:
	"""
	:param structure: list with tree structure
	:return: total number of dirs, files and links
	"""
	dirs, files, links = 0, 0, 0

	for item in structure:
		if isinstance(item, str):
			if os.path.islink(item):
				links += 1
			elif os.path.isdir(item):
				dirs += 1
			elif os.path.isfile(item):
				files += 1
		elif isinstance(item, list):
			sub_dirs, sub_files, sub_links = count_entries(item)
			dirs += sub_dirs
			files += sub_files
			links += sub_links

	return dirs, files, links


def print_tree(structure: list, prefix: str, output_stream):
	"""
	:param structure: list with tree structure
	:param prefix: prefix for output stream
	:param output_stream: file descriptor or stream object for output
	"""
	for item in structure:
		if isinstance(item, str):
			print_entry(os.path.basename(item), os.path.join(item, ".."), prefix, item is structure[-1], output_stream)
		elif isinstance(item, list):
			print_entry(os.path.basename(item[0]), os.path.join(item[0], ".."), prefix, item is structure[-1],
				output_stream)
			print_tree(item[1:], prefix + (PIPE if not (item is structure[-1]) else BLANK), output_stream)


def print_entry(name: str, path_prefix: str, prefix: str, is_last: bool, output_stream):
	"""
	:param name: name of object in parent directory
	:param path_prefix: full path to parent directory
	:param prefix: print prefix
	:param is_last: flag, that set to true when object is last in parent directory
	:param output_stream: file descriptor or stream object for output
	"""
	full_path = os.path.join(path_prefix, name)

	print(f"{prefix}{ELBOW if is_last else TEE}", end="", file=output_stream)
	print(f"{get_output_color(full_path)}{name}", end="", file=output_stream)

	if os.path.islink(full_path):
		print(f" -> {os.path.realpath(full_path)}", end="", file=output_stream)

	print(Style.RESET_ALL, file=output_stream)


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
