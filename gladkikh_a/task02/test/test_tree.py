import os
import shutil
import subprocess
import tempfile
import pytest
from task02.tree import generate_tree

class TestDirectoryTreeGenerator:
    @pytest.fixture
    def temp_dir(self, request):
        temp_dir = tempfile.mkdtemp()

        def cleanup():
            shutil.rmtree(temp_dir)

        request.addfinalizer(cleanup)
        return temp_dir

    def test_directory_tree_generation(self, temp_dir):
        script_file = "../src/tree.py"

        test_structure = {
            "root": {
                "dir1": {
                    "file1.txt": "",
                    "file2.txt": ""
                },
                "dir2": {
                    "file3.txt": ""
                },
                "file4.txt": ""
            }
        }

        generate_tree(temp_dir, test_structure)

        output_file_path = os.path.join(temp_dir, "output.txt")

        with open(output_file_path, "w") as output_file:
            import sys
            original_stdout = sys.stdout
            sys.stdout = output_file

            try:
                command = f"python {script_file} -H 2 {temp_dir.replace(os.sep, '\\\\')}"
                subprocess.run(command, shell=True, check=True)
            finally:
                sys.stdout = original_stdout

        print(f"Output for this test written to: {output_file_path}")