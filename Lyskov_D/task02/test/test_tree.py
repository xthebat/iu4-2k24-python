import os

import pytest

from tree import find_dir_and_files


@pytest.mark.parametrize(
    "start_path, max_level, expected",
    [
        [os.path.join(os.getcwd(), "..", "dir_for_tests"), 1, (['\x1b[34m|dir_for_tests/'], 1, 0)],
        [os.path.join(os.getcwd(), "..", "dir_for_tests"), 10, (['\x1b[34m|dir_for_tests/',
                                                                 '\x1b[34m|----test1/',
                                                                 '\x1b[32m|--------test1.txt',
                                                                 '\x1b[34m|----test2/',
                                                                 '\x1b[32m|--------test2.txt',
                                                                 '\x1b[32m|--------test22.txt'],
                                                                3,
                                                                3)]
    ]
)
def test_find_dir_and_files(start_path: str, max_level: int, expected: list[str]):
    assert find_dir_and_files(start_path, max_level) == expected
