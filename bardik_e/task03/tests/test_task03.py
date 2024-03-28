from io import StringIO

import pytest
import os

from src.task03.structures import SMDDocument
from src.task03.convert import MovementSMDConverter


def get_file_pair(sample_name: str) -> tuple[str, str]:
	test_dir = os.path.dirname(__file__)

	with (open(os.path.join(test_dir, "sources", sample_name), "r") as source,
	      open(os.path.join(test_dir, "results", sample_name), "r") as result):
		return source.read(), result.read()


@pytest.mark.parametrize(
	"file_name", os.listdir(os.path.join(os.path.dirname(__file__), "sources"))
)
def test_pass_doc(file_name: str) -> None:
	source, expected = get_file_pair(file_name)

	doc = SMDDocument.from_string(source)
	doc = MovementSMDConverter.convert(doc)

	text_stream = StringIO()
	text_stream.writelines(doc.to_string())

	assert text_stream.getvalue() == expected
