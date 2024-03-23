from pathlib import Path
import pytest
from src.main_tree import tree_list_create


@pytest.fixture
def create_temporary_directory(tmp_path) -> Path:
    """
    Creating test dir

    return value:  
        "└── root",
        "    ├── subdir2",
        "    │   ├── file3.txt",
        "    │   └── file4.txt",
        "    ├── subdir1",
        "    │   └── file2.txt",
        "    └── file1.txt"
    """
    root_dir = tmp_path / "root"
    root_dir.mkdir()
    (root_dir / "file1.txt").write_text("Content of file1")
    subdir1 = root_dir / "subdir1"
    subdir1.mkdir()
    (subdir1 / "file2.txt").write_text("Content of file2")
    subdir2 = root_dir / "subdir2"
    subdir2.mkdir()
    (subdir2 / "file3.txt").write_text("Content of file3")
    (subdir2 / "file4.txt").write_text("Content of file4")
    return tmp_path


def test_tree(create_temporary_directory) -> None:
    """Test without level flag"""
    directory_path = create_temporary_directory
    result = tree_list_create(path_name=directory_path,
                              result=[], level=-1, lvl_mod=False)
    expected_result = [
        "└── root",
        "    ├── subdir2",
        "    │   ├── file3.txt",
        "    │   └── file4.txt",
        "    ├── subdir1",
        "    │   └── file2.txt",
        "    └── file1.txt"
    ]
    assert result == expected_result


def test_tree_with_level_mod(create_temporary_directory):
    """Test with level flag"""
    directory_path = create_temporary_directory
    result = tree_list_create(path_name=directory_path,
                              result=[], level=2, lvl_mod=True)
    expected_result = [
        "└── root",
        "    ├── subdir2",
        "    ├── subdir1",
        "    └── file1.txt",
    ]
    assert result == expected_result
