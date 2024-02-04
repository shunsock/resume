import csv
from typing import List

from pydantic import HttpUrl

from resumer.domain.blog_article.blog_article_model import BlogArticleModel
from resumer.infrastracture.read_blog_article_csv.dto.read_blog_article_csv_dto import (
    ReadBlogArticleFromCsvDto,
)


def read_blog_article_from_csv(
    dto: ReadBlogArticleFromCsvDto,
) -> List[BlogArticleModel]:
    """Reads blog articles from a CSV file."""
    with open(str(dto.file_path), "r") as f:
        reader = csv.reader(f)
        next(reader)
        blog_articles = [
            BlogArticleModel(
                blog_service_name=dto.blog_service_name,
                title=row[0],
                url=HttpUrl(row[1]),
            )
            for row in reader
        ]

        return blog_articles
