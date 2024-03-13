import argparse

import pytest
from colorama import Fore, Style

from task02.task02 import (
    generate_string,
    range_type,
)

CROWBAR = '└──'
T_LEFT = '├──'
LINE = '│    '
BLANK = '     '


@pytest.mark.parametrize(
    "is_dir, is_last, name, expected",
    [
        [True, True, "papka", f"{CROWBAR} {Fore.BLUE}papka{Style.RESET_ALL}"],
        [False, False, "wadawd.txt", f"{T_LEFT} {Fore.GREEN}wadawd.txt{Style.RESET_ALL}"],
    ]
)
def test_generate_string(is_dir: str, is_last: bool, name: str, expected: str) -> str:
    assert generate_string(is_dir, is_last, name) == expected


@pytest.mark.parametrize(
    "astr, min, max, expected",
    [
        [10, 0, 100, 10],
        [100, 0, 200, 100],
    ]
)
def test_range_type(astr: str, min: int, max: int, expected) -> int:
    assert range_type(astr, min, max) == expected

@pytest.mark.xfail(raises=argparse.ArgumentTypeError)
def test2_range_type() -> int:
    range_type(-20, 0, 100)