from typing import List
import os


def get_path_list(directory: str) -> List[str]:
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
        raise TypeError('directory must be a string')
    if os.path.isdir(directory) is False:
        raise NotADirectoryError('directory must be a valid directory')

    txt_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
    return txt_files


def get_file_contents(file_path: str) -> List[str]:
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
        raise TypeError('file_path must be a string')
    if os.path.isfile(file_path) is False:
        raise FileNotFoundError('file_path must be a valid file')

    with open(file_path, 'r') as f:
        return f.readlines()


if __name__ == '__main__':
    files: List[str] = get_path_list('src/profile/')
    with open('README.md', 'a') as readme:
        for f in files:
            lines: List[str] = sorted(get_file_contents(f))
            for line in lines:
                # print(line)
                readme.write(line + '\n')
