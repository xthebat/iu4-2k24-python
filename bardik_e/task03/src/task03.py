import argparse
import os

from task03.convert import MovementSMDConverter
from task03.structures import SMDDocumentFabric

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Studio Model Data files converter.")
	parser.add_argument("path", type=str, nargs=1, help="Path to convertible file.")
	parser.add_argument("--output", type=str, default="", help="Path to output file.")
	args = parser.parse_args()

	source_path = args.path[0]

	if not os.path.isfile(source_path):
		parser.error("file with provided path does not exist.")

	try:
		with open(source_path, "r") as f:
			doc = SMDDocumentFabric().create_document(f.read())

		converter = MovementSMDConverter(doc)

		if len(args.output):
			converter.file_path = args.output

		converter.convert()
		converter.save()

	except PermissionError:
		raise PermissionError("Unable to open file for converted output.")
