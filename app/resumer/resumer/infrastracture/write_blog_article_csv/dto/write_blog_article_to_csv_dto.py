from typing import List

from pydantic import BaseModel, FilePath

from resumer.domain.blog_article.blog_article_model import BlogArticleModel


class WriteBlogArticleToCsvDto(BaseModel):
    """Data transfer object for writing blog articles to a CSV file."""

    file_path: FilePath
    blog_articles: List[BlogArticleModel]
