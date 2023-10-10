import os
from typing import List

from src.models.article import Article
from src.service.article_handler import read_articles_list_from_csv


def run(file_path: str, site_name: str, tag_name: str) -> None:
    """
    Converts a csv file to a text file

    Parameters
    ======
    file_path: str

    Returns
    ======
    None

    Raises
    ======
    TypeError: if file_path is not a string
    FileNotFoundError: if file_path is not a valid file
    """
    if isinstance(file_path, str) is False:
        raise TypeError("file_path must be a string")
    if os.path.isfile(file_path) is False:
        raise FileNotFoundError("file_path must be a valid file")

    articles = read_articles_list_from_csv(file_path)

    # revese to assign the latest article at the top
    articles_reverse: List[Article] = articles[::-1]
    with open("README.md", "a") as f:
        for article in articles_reverse:
            title = "[" + article.title + "](" + str(article.link) + ")"
            row = "|" + site_name + "|" + tag_name + "|" + title + "|\n"
            f.write(row)
