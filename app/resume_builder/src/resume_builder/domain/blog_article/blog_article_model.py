from pydantic import BaseModel, HttpUrl, StrictStr

from src.resume_builder.domain.blog_article.get_blog_article_csv_path import (
    get_blog_article_csv_path,
)


class BlogArticleModel(BaseModel):
    """
    Blog article model
    title: StrictStr - article title
    url: StrictStr - article URL
    """

    blog_service_name: StrictStr
    title: StrictStr
    url: HttpUrl

    def get_blog_article_csv_path(self) -> str:
        """Returns the file path of the CSV."""
        return get_blog_article_csv_path(self.blog_service_name)
