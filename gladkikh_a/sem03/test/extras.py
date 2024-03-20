import os.path

dir_base_path = os.path.dirname(os.path.abspath(__file__))
extras_base_path = os.path.join(dir_base_path, ".extras")


def get_filepath(filename: str) -> str:
    filepath = os.path.join(extras_base_path, filename)
    if not os.path.isfile(filepath):
        raise ValueError(f"Test extras file isn't exist: '{filename}'")
    return filepath


__all__ = ["get_filepath"]
