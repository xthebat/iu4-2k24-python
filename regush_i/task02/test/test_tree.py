""" Test for tree module"""

from pathlib import Path
from src.tree import tree
import pytest


@pytest.fixture
def tmp_dir_fixture(tmp_path) -> Path:
    """Creating test dir"""
    root_dir = tmp_path / "main_dir"
    root_dir.mkdir()
    (root_dir / "file1.txt").write_text("Content of file1")
    subdir1 = root_dir / "sub1"
    subdir1.mkdir()
    (subdir1 / "file2.txt").write_text("Content of file2")
    subsubdir1 = subdir1 / "subsub1"
    subsubdir1.mkdir()
    (subsubdir1 / "file3.txt").write_text("Content of file3")
    (subsubdir1 / "file4.txt").write_text("Content of file4")
    subdir2 = root_dir / "sub2"
    subdir2.mkdir()
    (subdir2 / "file6.txt").write_text("Content of file5")
    (subdir2 / "file6.txt").write_text("Content of file6")
    return tmp_path


@pytest.mark.parametrize(
    "level, expected",
    [
        [-1, """└──main_dir
    ├──file1.txt
    ├──sub2
    │   └──file6.txt
    └──sub1
        ├──subsub1
        │   ├──file3.txt
        │   └──file4.txt
        └──file2.txt"""],
        [0, """"""],
        [1, """└──main_dir"""],
        [2, """└──main_dir
   ├──file1.txt
   ├──sub2
   └──sub1"""],
        [3, """└──main_dir
   ├──file1.txt
   ├──sub2
   │  └──file6.txt
   └──sub1
      ├──subsub1
      └──file2.txt"""],
        [4, """└──main_dir
   ├──file1.txt
   ├──sub2
   │  └──file6.txt
   └──sub1
      ├──subsub1
      │  ├──file3.txt
      │  └──file4.txt
      └──file2.txt"""],

    ]
)
def test_tree(tmp_dir_fixture, level, expected):
    """ Test for tree func """
    dir_path = str(tmp_dir_fixture)
    tr = tree(dir_path, level)
    print(tr)
    assert tr == expected
