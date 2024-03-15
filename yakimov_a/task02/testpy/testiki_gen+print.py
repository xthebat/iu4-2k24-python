import sys
import pytest
from io import StringIO
from scripts.tree import gen_tree, print_tree

@pytest.fixture
def captured_output():
    # capture output
    capture = StringIO()
    sys.stdout = capture
    yield capture
    sys.stdout = sys.__stdout__

@pytest.mark.parametrize("path_depth", open("testpy/data_for_test/file_1copy.txt"))
def test_gen_tree(path_depth, captured_output):
    path, depth = path_depth.strip().split(" - ")
    result = gen_tree(path, int(depth))
    assert result
    #test func
    print_tree(result)
    # get capture data
    output = captured_output.getvalue()
    # check data
    expected_output = ("|-- Микита\n  |-- Лаб\n  |-- Семы\n")
    expected_output = expected_output.strip()
    assert output == expected_output
