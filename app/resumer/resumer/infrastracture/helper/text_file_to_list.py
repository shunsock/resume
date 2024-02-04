from typing import List


def text_file_to_list(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        return f.readlines()
