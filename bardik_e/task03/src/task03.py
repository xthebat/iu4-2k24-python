import argparse
import os

from task03.convert import MovementSMDConverter
from task03.structures import SMDDocument


def main():
	parser = argparse.ArgumentParser(description="Studio Model Data files converter.")
	parser.add_argument("path", type=str, nargs=1, help="Path to convertible file.")
	parser.add_argument("--output", type=str, default="", help="Path to output file.")
	args = parser.parse_args()

	source_path = args.path[0]

	if not os.path.isfile(source_path):
		parser.error("file with provided path does not exist.")

	try:
		with open(source_path, "rt") as input_file:
			doc = SMDDocument.from_string(input_file.read())

	except PermissionError:
		raise PermissionError(f"Unable to open file ({source_path}) for reading.")

	doc = MovementSMDConverter.convert(doc)
	output_path = args.output[0] if len(args.output) else os.path.join(os.getcwd(), "result.smd")

	try:
		with open(output_path, "wt") as output_file:
			output_file.writelines(doc.to_string())

	except PermissionError:
		raise PermissionError(f"Unable to open file ({output_path}) for output write.")


if __name__ == '__main__':
	main()
