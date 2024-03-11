import os
import shutil


def create_structure(base_path: str, structure_content: list) -> None:
    """
    Creates directory structure and files based on the given content list.

    Args:
        base_path (str): The base path where the structure will be created.
        structure_content (list): The content list specifying the directory structure and files.
    """
    if len(structure_content) == 0:
        return
    dir_name = structure_content[0]
    if os.path.exists(os.path.join(base_path, dir_name)):
        remove_structure(base_path, dir_name)

    dir_path = os.path.join(base_path, dir_name)
    os.makedirs(dir_path)
    for item in structure_content[1:]:
        if isinstance(item, str):
            with open(os.path.join(dir_path, item), 'w'):
                pass
        elif isinstance(item, list):
            create_structure(dir_path, item)


def remove_structure(base_path: str, content_structure: str) -> None:
    """
    Remove the directory structure specified by the content_structure from the base_path.

    Args:
        base_path (str): The base path where the structure is located.
        content_structure (str): The name of the directory structure to remove.
    """
    dir_path = os.path.join(base_path, content_structure)

    try:
        shutil.rmtree(dir_path)
    except FileNotFoundError:
        return
