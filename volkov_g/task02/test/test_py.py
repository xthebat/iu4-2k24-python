import pytest
# import os

from src.task02.main import function_sample
from src.task02.main import dir_control


@pytest.mark.parametrize(
    "x,y,expected",
    [
        [1, 1, 2],
        [1, -1, 0],
        [10, 9, 19]
    ]
)
def test_function_sample(x: int, y: int, expected: int):
    assert function_sample(1, 2) == 3


@pytest.mark.parametrize(
    "putin,depth,expected",
    [
        ["test flobers", 1, 3],
        ["test flobers", 2, 12],
        ["test flobers", 3, 13]
    ]
)
def test_dir_control(putin: str, depth: int, expected: int):
    print("")
    assert dir_control(putin, depth) == expected
