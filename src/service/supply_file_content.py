import os
from typing import List


def get(file_path: str) -> List[str]:
    """
    Returns the contents of a file

    Parameters
    ======
    file_path: str

    Returns
    ======
    str

    Raises
    ======
    TypeError: if file_path is not a string
    FileNotFoundError: if file_path is not a valid file
    """
    if isinstance(file_path, str) is False:
        raise TypeError("file_path must be a string")
    if os.path.isfile(file_path) is False:
        raise FileNotFoundError("file_path must be a valid file")

    with open(file_path, "r") as f:
        return f.readlines()
