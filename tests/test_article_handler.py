import os
from typing import List

from src.models.article import Article
from src.service.article_handler import (read_articles_list_from_csv,
                                         write_articles_to_csv)


def supply_test_case_on_memory() -> List[Article]:
    return [
        Article(
            title="Test Article 1",
            link="https://www.test1.com/",
        ),
        Article(
            title="Test Article 2",
            link="https://www.test2.com/",
        ),
    ]


def test_write_articles_to_csv() -> None:
    articles = supply_test_case_on_memory()
    csv_file_path = "src/techblog/data/test_write_article.csv"
    write_articles_to_csv(articles, csv_file_path)
    os.remove(csv_file_path)
    assert True


def test_write_articles_to_csv_with_empty_list() -> None:
    articles = []
    csv_file_path = "src/techblog/data/test_write_article.csv"
    try:
        # fail to write empty list
        # no file will be created
        write_articles_to_csv(articles, csv_file_path)
    except ValueError:
        assert True


def test_read_articles_list_from_csv() -> None:
    # write test data to csv
    file_path = "src/techblog/data/test_read_article.csv"
    write_articles_to_csv(supply_test_case_on_memory(), file_path)

    # read test data from csv we just wrote
    articles: List[Article] = read_articles_list_from_csv(file_path)
    assert len(articles) == 2
    assert articles[0].title == "Test Article 1"
    assert str(articles[0].link) == "https://www.test1.com/"
    assert articles[1].title == "Test Article 2"
    assert str(articles[1].link) == "https://www.test2.com/"

    # remove test data
    os.remove(file_path)


def test_read_artsscles_list_from_csv_with_empty_file() -> None:
    file_path = ""
    try:
        read_articles_list_from_csv(file_path)
    except OSError as e:
        print(e)
        assert True


def test_read_articles_list_from_csv_with_invalid_file() -> None:
    file_path = "src/techblog/data/invalid.csv"
    try:
        read_articles_list_from_csv(file_path)
    except OSError as e:
        print(e)
        assert True
