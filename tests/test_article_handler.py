from models.article import Article
from typing import List
from service.article_handler import write_articles_to_csv


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
    csv_file_path="techblog/test.csv"
):
    write_articles_to_csv(articles, csv_file_path)
    assert True


def test_write_articles_to_csv_with_empty_list(
    articles=[],
    csv_file_path="techblog/test.csv"
):
    write_articles_to_csv(articles, csv_file_path)
    assert True
