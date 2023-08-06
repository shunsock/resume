from typing import List
from models.article import Article
import csv


def write_articles_to_csv(articles: List[Article], filename: str) -> None:
    # input validation
    if isinstance(articles, List) is False:
        raise TypeError("Articles must be a list")
    if isinstance(filename, str) is False:
        raise TypeError("Filename must be a string")
    if len(articles) == 0:
        raise ValueError("No articles to write to CSV")
    if filename == "":
        raise ValueError("No filename provided")

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['title', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for article in articles:
            writer.writerow(article.model_dump())
