import os
from typing import List


def get(directory: str) -> List[str]:
    """
    Returns a list of all .txt files in a directory

    Parameters
    ======
    directory: str

    Returns
    ======
    List[str]

    Raises
    ======
    TypeError: if directory is not a string
    NotADirectoryError: if directory is not a valid directory
    """
    if isinstance(directory, str) is False:
        raise TypeError("directory must be a string")
    if os.path.isdir(directory) is False:
        raise NotADirectoryError("directory must be a valid directory")

    txt_files = [
        os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".txt")
    ]
    return txt_files
