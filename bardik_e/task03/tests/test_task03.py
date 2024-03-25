import pytest
import os
from pathlib import Path

from src.task03.convert import MovementSMDConverter
from src.task03.structures import SMDDocumentFabric


def get_file_pair(sample_name: str) -> tuple[str, str]:
	test_dir = os.path.dirname(__file__)

	with (open(os.path.join(test_dir, "sources", sample_name), "r") as source,
		open(os.path.join(test_dir, "results", sample_name), "r") as result):
		return source.read(), result.read()


@pytest.mark.parametrize(
	"file_name", os.listdir(os.path.join(os.path.dirname(__file__), "sources"))
)
def test_pass_doc(file_name: str, tmp_path: Path) -> None:
	source, expected = get_file_pair(file_name)
	doc = SMDDocumentFabric().create_document(source)
	converter = MovementSMDConverter(doc)

	converter.file_path = tmp_path / f"{file_name}_test.smd"

	converter.convert()
	converter.save()

	with open(converter.file_path, "r") as result:
		assert result.read() == expected
