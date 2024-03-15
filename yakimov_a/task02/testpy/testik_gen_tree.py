import pytest
from scripts.tree import gen_tree

@pytest.mark.parametrize("path_depth", open("testpy/data_for_test/file_1.txt"))
def test_gen_tree(path_depth):
    path, depth = path_depth.strip().split(" - ")
    result = gen_tree(path, int(depth))
    assert result