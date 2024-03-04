import pytest
import sys, os
from colorama import Fore

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from tree import Tree

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


def read_test_suite(suite_path : str) -> str:
    with open(suite_path, "r") as f:
        f_str = f.read()

    return f_str


def cmp_expected_and_real(suite_path : str, capsys, create_filesystem) ->None:
    tree = Tree()
    tree.print()

    captured = capsys.readouterr() # Захват stdout и stderr в строку
    expected_str = read_test_suite(suite_path)
    expected_str = expected_str.format(head_dir=create_filesystem, blue=Fore.BLUE, reset=Fore.RESET)
    
    assert captured.out == expected_str


def test_tree(create_filesystem, monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["", f"{create_filesystem}"])
    cmp_expected_and_real("suites/test_tree.txt", capsys, create_filesystem)    


def test_tree_asc(create_filesystem, monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["", f"{create_filesystem}", "-s", "asc"])
    cmp_expected_and_real("suites/test_tree_asc.txt", capsys, create_filesystem)


def test_tree_desc(create_filesystem, monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["", f"{create_filesystem}", "-s", "desc"])
    cmp_expected_and_real("suites/test_tree_desc.txt", capsys, create_filesystem)

def test_tree_depth(create_filesystem, monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["", f"{create_filesystem}", "-d", "2"])
    cmp_expected_and_real("suites/test_tree_depth.txt", capsys, create_filesystem)