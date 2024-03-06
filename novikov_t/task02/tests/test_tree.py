import os
import sys
import pytest
from src.tree import generate_tree, print_tree


@pytest.mark.parametrize(
    argnames="dir_number, depth, referent_file",
    argvalues=[
        [1, 1, "referents/referent_1.txt"],
        [1, 2, "referents/referent_2.txt"],
        [2, 1, "referents/referent_3.txt"]
    ]
)
def test_generate_tree(dir_number: int, depth: int, referent_file: str):
    # temporary directories and files for the test
    test_dir = 'test_directory'
    test_file1 = os.path.join(test_dir, 'file1.txt')
    test_file2 = os.path.join(test_dir, 'file2.txt')
    test_dir_2 = os.path.join(test_dir, test_dir)
    test_file3 = os.path.join(test_dir_2, "file3.txt")

    try:
        # create directories and files
        os.makedirs(test_dir)
        with open(test_file1, 'w'):
            pass
        with open(test_file2, 'w'):
            pass
        os.makedirs(test_dir_2)
        with open(test_file3, 'w'):
            pass

        original_stdout = sys.stdout
        # redirect cout to a file output.txt
        with open('output.txt', 'w', encoding='utf-8') as test_output:
            sys.stdout = test_output
            # fill in the file with the output of the tree()
            print_tree(generate_tree(
                test_dir if dir_number == 1 else test_dir_2, depth))
        sys.stdout = original_stdout

        # get path to the referent file
        path_to_test_script = os.path.realpath(__file__)
        path_to_referent = os.path.join(
            os.path.dirname(path_to_test_script), referent_file)
        # check if the function is working as intended
        with open('output.txt', 'rb') as test_out, open(path_to_referent, 'rb') as ref:
            assert test_out.read() == ref.read()

    finally:
        # delete temporary files and directory
        os.remove("output.txt")
        os.remove(test_file3)
        os.rmdir(test_dir_2)
        os.remove(test_file1)
        os.remove(test_file2)
        os.rmdir(test_dir)
