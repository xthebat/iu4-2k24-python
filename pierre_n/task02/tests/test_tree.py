import os
import pytest
import sys
import shutil
import tempfile
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.task02.tree import get_directory_tree, display_tree

@pytest.fixture
def temp_directory():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def temp_files(temp_directory):
    temp_file1 = os.path.join(temp_directory, "tempf1.txt")
    temp_file2 = os.path.join(temp_directory, "tempf2.txt")
    temp_file3 = os.path.join(temp_directory, "tempf3.txt")
    with open(temp_file1, 'w') as f1, open(temp_file2, 'w') as f2, open(temp_file3, 'w') as f3:
        f1.write("Temporary file 1")
        f2.write("Temporary file 2")
        f3.write("Temporary file 3")
    return temp_file1, temp_file2, temp_file3

def test_display_tree(temp_directory, temp_files, capsys):
    tree = get_directory_tree(temp_directory)
    display_tree(tree)

    captured = capsys.readouterr()
    expected_output = f"├── \x1b[32mtempf1.txt\n├── \x1b[32mtempf2.txt\n└── \x1b[32mtempf3.txt\n"
    assert captured.out == expected_output

if __name__ == "__main__":
    pytest.main()