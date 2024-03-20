import pytest
import sys, os
from colorama import Fore

TEST_DIR = os.path.dirname(__file__)
MODULE_DIR = os.path.join(TEST_DIR, '..', 'src')
TEST_SUITE_DIR = "suites"
TEST_TREE_SUITE = "test_tree.txt"
TEST_TREE_ASC_SUITE = "test_tree_asc.txt"
TEST_TREE_DESC_SUITE = "test_tree_desc.txt"
TEST_TREE_DEPTH_SUITE = "test_tree_depth.txt"

sys.path.append(MODULE_DIR)

from tree import Tree, TreeException

@pytest.fixture
def create_filesystem(tmp_path):  
    for i in range(1, 4):
        dir_name =  tmp_path / f"dir_{i}"
        dir_name.mkdir()

        for i in range(1, 4):
            file_name =  dir_name / f"file_{i}.txt"
            file_name.touch()

        for i in range(1, 4):
            dir_name1 =  dir_name / f"dir_{i}"
            dir_name1.mkdir()

            for i in range(1, 4):
                file_name1 =  dir_name1 / f"file_{i}.txt"
                file_name1.touch()

    return tmp_path

def read_test_suite(test_suite: str) -> str:
    with open(os.path.join(TEST_DIR, TEST_SUITE_DIR, test_suite), "r") as f:
        f_str = f.read()

    return f_str

@pytest.mark.parametrize(
    "suite,depth,sort",
    [
        (TEST_TREE_SUITE, None, None),
        (TEST_TREE_ASC_SUITE, None, "asc"),
        (TEST_TREE_DESC_SUITE, None, "desc"),
        (TEST_TREE_DEPTH_SUITE, 2, None)
    ]
)
def test_tree_build(create_filesystem, capsys, suite: str, depth: int, sort: str):
    tree = Tree()
    tree.build(create_filesystem, depth, sort)

    actual = capsys.readouterr().out
    expected = read_test_suite(suite)
    expected = expected.format(head_dir=create_filesystem, blue=Fore.BLUE, reset=Fore.RESET)
    
    assert actual == expected

@pytest.mark.parametrize(
    "depth,sort,expected",
    [
        (-1, None, "-1 is an incorrect depth!"),
        (None, "gav", "gav is an incorrect sort option!")
    ]
)
def test_bad_parameters(create_filesystem, depth: int, sort: str, expected: str):
    with pytest.raises(TreeException) as exc_info:
        tree = Tree()
        tree.build(create_filesystem, depth, sort)
        actual = str(exc_info.value)
        assert actual == expected