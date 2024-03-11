import pytest
# import os

from src.task02.main import tree_dir


@pytest.mark.parametrize(
    "path,depth,folders,file",
    [
        ["test folders", 1, 3, 0],
        ["test folders", 2, 12, 0],
        ["test folders", 3, 14, 2]
    ]
)
def test_dir_control(path: str, depth: int, folders: int, file: int):
    print("")
    assert tree_dir(path, depth)[0:2] == [folders, file]
