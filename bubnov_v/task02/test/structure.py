import os
import shutil
from colorama import Fore, Style


# Creating a structure of files
def create_structure(base_path: str, structure_content: list) -> None:
    # Handler error path exist
    if os.path.exists(os.path.join(base_path, structure_content[0][0])):
        print(f"{Fore.RED}DIRECTORY EXIST {base_path}{Style.RESET_ALL}")
        return
    # Create structure directories and files
    for item in structure_content:
        if type(item) is str:
            with open(os.path.join(base_path, item), 'w'):
                pass
        elif type(item) is list:
            dir_name = item[0]
            dir_path = os.path.join(base_path, dir_name)
            os.makedirs(dir_path)
            if len(item) > 1:
                create_structure(dir_path, item[1:])


# Remove a structure of files
def remove_structure(base_path: str, directory: list) -> None:
    directory = directory[0][0]
    base_path = os.path.join(base_path, directory)
    # Handler error not found
    try:
        shutil.rmtree(base_path)
    except FileNotFoundError:
        print(f"{Fore.RED}DIRECTORY NOT FOUND {base_path}{Style.RESET_ALL}")
        return
