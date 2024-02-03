import csv

from src.resume_builder.domain.blog_article.get_blog_article_csv_header import (
    get_blog_article_csv_header,
)
from src.resume_builder.infrastracture.write_blog_article_csv.dto.write_blog_article_to_csv_dto import (
    WriteBlogArticleToCsvDto,
)


def write_blog_article_to_csv(dto: WriteBlogArticleToCsvDto) -> None:
    """Writes blog articles to a CSV file."""
    with open(str(dto.file_path), "w") as f:
        writer = csv.writer(f)
        writer.writerow(get_blog_article_csv_header())
        for article in dto.blog_articles:
            writer.writerow([article.title, article.url])  # type: ignore
