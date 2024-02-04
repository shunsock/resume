import pytest

from resumer.domain.blog_article.blog_article_model import BlogArticleModel
from resumer.infrastracture.read_blog_article_csv.dto.read_blog_article_csv_dto import (
    ReadBlogArticleFromCsvDto,
)
from resumer.infrastracture.read_blog_article_csv.read_blog_article_from_csv import (
    read_blog_article_from_csv,
)


@pytest.mark.parametrize(
    "dto",
    [
        ReadBlogArticleFromCsvDto(
            blog_service_name="hatena_blog",
            file_path="resumer/data/blog_article/hatena_blog.csv",
        ),
        ReadBlogArticleFromCsvDto(
            blog_service_name="prtimes_tech_blog",
            file_path="resumer/data/blog_article/prtimes_tech_blog.csv",
        ),
        ReadBlogArticleFromCsvDto(
            blog_service_name="zenn",
            file_path="resumer/data/blog_article/zenn.csv",
        ),
        ReadBlogArticleFromCsvDto(
            blog_service_name="toukei_no_mori",
            file_path="resumer/data/blog_article/toukei_no_mori.csv",
        ),
    ],
)
def test_read_blog_article_from_csv(dto: ReadBlogArticleFromCsvDto):
    blog_articles = read_blog_article_from_csv(dto)

    for blog_article in blog_articles:
        print(type(blog_article))
        assert isinstance(blog_article, BlogArticleModel)
        assert blog_article.blog_service_name == dto.blog_service_name
        assert blog_article.title
        assert blog_article.url
        assert blog_article.get_blog_article_csv_path()
