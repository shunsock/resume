from typing import List

from pydantic import BaseModel

from resumer.domain.blog_article.blog_article_model import BlogArticleModel


class WriteBlogArticleToReadmeDto(BaseModel):
    output_file_path: str
    articles: List[BlogArticleModel]
