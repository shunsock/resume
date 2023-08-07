from typing import List

from src.models.article import Article
from src.service.article_handler import write_articles_to_csv


def supply_test_case_on_memory() -> List[Article]:
    return [
        Article(
            title="Test Article 1",
            link="http://www.test1.com/",
        ),
        Article(
            title="Test Article 2",
            link="http://www.test2.com/",
        ),
    ]


def test_write_articles_to_csv(
    articles=supply_test_case_on_memory(), csv_file_path="src/techblog/data/test.csv"
):
    write_articles_to_csv(articles, csv_file_path)
    assert True


def test_write_articles_to_csv_with_empty_list(
    articles=[], csv_file_path="src/techblog/data/test.csv"
):
    try:
        write_articles_to_csv(articles, csv_file_path)
    except ValueError as e:
        assert True
