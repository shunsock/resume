import csv
import os
from typing import List
from src.models.article import Article


def write_articles_to_csv(articles: List[Article], filename: str) -> None:
    """
        Write articles to CSV file

        Parameters
        ======
        articles: List[Article]
        filename: str

        Returns
        ======
        None

        Raises
        ======
        TypeError: articles is not a list
        TypeError: filename is not a string
        ValueError: articles is empty
        ValueError: filename is empty
    """
    # input validation
    if isinstance(articles, List) is False:
        raise TypeError("Articles must be a list")
    if isinstance(filename, str) is False:
        raise TypeError("Filename must be a string")
    if len(articles) == 0:
        raise ValueError("No articles to write to CSV")
    if filename == "":
        raise ValueError("No filename provided")

    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["title", "link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for article in articles:
            writer.writerow(article.model_dump())


def read_articles_list_from_csv(file_path: str) -> List[Article]:
    """
        Read articles from CSV file

        Parameters
        ======
        file_path: str

        Returns
        ======
        List[Article]

        Raises
        ======
        TypeError: file_path is not a string
        OSError: file_path is not a file
        ValueError: articles is empty
    """
    # input validation
    if isinstance(file_path, str) is False:
        raise TypeError("File path must be a string")
    if os.path.isfile(file_path) is False:
        raise OSError("File path must be a file")

    # read CSV
    articles: List[Article] = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            articles.append(Article.model_validate(row))

    # validation
    if len(articles) == 0:
        raise ValueError("No articles to read from CSV")

    return articles
