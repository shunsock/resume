from src.service.article_handler.article_supply import ArticleSupply
from src.service.article_handler.read_articles_list_from_csv import read_articles_list_from_csv
import os


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

    articles = ArticleSupply(read_articles_list_from_csv(file_path))
    with open("README.md", "a") as f:
        for article in articles.articles:
            title = "[" + article.title + "](" + str(article.link) + ")"
            row = "|" + site_name + "|" + tag_name + "|" + title + "|\n"
            f.write(row)
