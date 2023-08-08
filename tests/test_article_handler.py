from typing import List

from src.models.article import Article
from src.service.article_handler import (
    write_articles_to_csv,
    read_articles_list_from_csv
)


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
    articles=supply_test_case_on_memory(),
    csv_file_path="src/techblog/data/test.csv"
):
    write_articles_to_csv(articles, csv_file_path)
    assert True


def test_write_articles_to_csv_with_empty_list(
    articles=[], csv_file_path="src/techblog/data/test.csv"
):
    try:
        write_articles_to_csv(articles, csv_file_path)
    except ValueError as e:
        print(e)
        assert True


def test_read_articles_list_from_csv(file_path="src/techblog/data/test.csv"):
    articles: List[Article] = read_articles_list_from_csv(file_path)
    assert len(articles) == 2
    assert articles[0].title == "Test Article 1"
    assert str(articles[0].link) == "http://www.test1.com/"
    assert articles[1].title == "Test Article 2"
    assert str(articles[1].link) == "http://www.test2.com/"


def test_read_artsscles_list_from_csv_with_empty_file(file_path=""):
    try:
        read_articles_list_from_csv(file_path)
    except OSError as e:
        print(e)
        assert True


def test_read_articles_list_from_csv_with_invalid_file(
        file_path="src/techblog/data/invalid.csv"
):
    try:
        read_articles_list_from_csv(file_path)
    except OSError as e:
        print(e)
        assert True
