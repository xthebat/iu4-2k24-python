import os
import pytest
from task02 import generate_tree, print_tree  # Replace 'myscript' with the actual name of your script

@pytest.mark.parametrize(
    "directory, depth, expected_output",
    [
        ("test_directory", 1, {"test_directory"}),
        ("test_directory", 2, {"test_directory", {"file1.txt", "file2.txt"}}),
        ("test_directory/test_directory", 1, {"test_directory", {"file1.txt", "file2.txt", {"file3.txt"}}}),
    ]
)
def test_generate_and_print_tree(tmp_path, directory, depth, expected_output):
    # Create a temporary directory for testing
    tmp_directory = tmp_path / directory
    tmp_directory.mkdir(parents=True)

    # Generate the tree
    generated_tree = generate_tree(tmp_directory, depth)

    # Redirect print output to a list
    printed_tree = []

    def mock_print(*args, **kwargs):
        printed_tree.extend(args)

    original_print = __builtins__["print"]
    __builtins__["print"] = mock_print

    try:
        # Print the tree
        print_tree(generated_tree)
    finally:
        # Restore the original print function
        __builtins__["print"] = original_print

    # Compare with the expected output using sets
    assert set(printed_tree) == expected_output
