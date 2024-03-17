import pytest
import os
import shutil
from pathlib import Path
from colorama import Fore, Style
from io import StringIO

from src.task02 import tree


@pytest.fixture()
def create_test_environment(tmp_path: Path) -> Path:
	dir_ = tmp_path / "dirs"
	dir_.mkdir()

	print(dir_)

	dir_1 = dir_ / "dir_1"
	dir_1.mkdir()

	dir_1_1 = dir_1 / "dir_1_1"
	dir_1_1.mkdir()
	dir_1_2 = dir_1 / "dir_1_2"
	dir_1_2.mkdir()

	dir_2 = dir_ / "dir_2"
	dir_2.mkdir()

	dir_2_1 = dir_2 / "dir_2_1"
	dir_2_1.mkdir()
	file_2_1_1 = dir_2_1 / "file_2_1_1"
	file_2_1_1.touch()
	file_2_1_2 = dir_2_1 / "file_2_1_2"
	file_2_1_2.touch()

	dir_2_2 = dir_2 / "dir_2_2"
	dir_2_2.mkdir()
	file_2_2_1 = dir_2_2 / "file_2_2_1"
	file_2_2_1.touch()

	dir_2_2_1 = dir_2_2 / "dir_2_2_1"
	dir_2_2_1.mkdir()

	dir_2_3 = dir_2 / "dir_2_3"
	dir_2_3.mkdir()
	file_2_3_1 = dir_2_3 / "file_2_3_1"
	file_2_3_1.touch()

	dir_3 = dir_ / "dir_3"
	dir_3.mkdir()
	file_3 = dir_3 / "file_3"
	file_3.touch()

	return tmp_path


def remove_test_environment(tmp_path: Path) -> None:
	shutil.rmtree(str(tmp_path), ignore_errors=True)


def read_test_reference(name: str) -> str:
	with open(os.path.join(os.getcwd(), "references", name), "r", encoding="utf-8") as f:
		return f.read()


@pytest.fixture(autouse=True)
def prepare_test_environment(create_test_environment) -> None:
	yield
	remove_test_environment(create_test_environment)


@pytest.mark.parametrize(
	"name,depth",
	[
		["base", -1],
		["depth_0", 0],
		["depth_2", 2]
	]
)
def test_run(name: str, depth: int, tmp_path: Path) -> None:
	out_stream = StringIO()
	temp_test_path = str(tmp_path / "dirs")

	tree.run(temp_test_path, depth, out_stream)
	result = out_stream.getvalue()
	expected = read_test_reference(f"reference_{name}.txt").format(
		blue=Fore.BLUE, green=Fore.GREEN, color_end=Style.RESET_ALL, root_dir=temp_test_path)

	assert expected == result
