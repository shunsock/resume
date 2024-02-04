from pathlib import Path
from typing import List

from resumer.domain.blog_article.blog_article_model import BlogArticleModel
from resumer.domain.blog_article.get_blog_article_csv_path import (
    get_blog_article_csv_path,
)
from resumer.domain.fetch_target_blog_service.zenn_rss_api import ZennRssApi
from resumer.infrastracture.fetch_zenn_rss.dto.fetch_zenn_rss_dto import FetchZennRssDto
from resumer.infrastracture.fetch_zenn_rss.zenn_rss_repository import fetch_zenn_rss
from resumer.infrastracture.fetch_zenn_rss.zenn_rss_response_text_to_model import (
    zenn_rss_response_text_to_model,
)
from resumer.infrastracture.read_blog_article_csv.dto.read_blog_article_csv_dto import (
    ReadBlogArticleFromCsvDto,
)
from resumer.infrastracture.read_blog_article_csv.read_blog_article_from_csv import (
    read_blog_article_from_csv,
)
from resumer.infrastracture.write_blog_article_csv.dto.write_blog_article_to_csv_dto import (
    WriteBlogArticleToCsvDto,
)
from resumer.infrastracture.write_blog_article_csv.write_blog_article_to_csv import (
    write_blog_article_to_csv,
)


def update_zenn() -> None:
    """
    fetching zenn articles and update csv file
    Returns:

    """
    zenn_rss_api: ZennRssApi = ZennRssApi()

    zenn_rss_xml: str = fetch_zenn_rss(dto=FetchZennRssDto())
    zenn_articles: List[BlogArticleModel] = zenn_rss_response_text_to_model(
        text=zenn_rss_xml
    )

    blog_service_name: str = zenn_rss_api.name
    current_zenn_csv: List[BlogArticleModel] = read_blog_article_from_csv(
        dto=ReadBlogArticleFromCsvDto(
            blog_service_name=blog_service_name,
            file_path=get_blog_article_csv_path(blog_service_name),
        )
    )

    for article in zenn_articles:
        print("checking:", article.title)
        if article not in current_zenn_csv:
            print("new article found")
            print("adding:", article.title)
            current_zenn_csv.append(article)
        else:
            print("already exists")

    article_sorted: List[BlogArticleModel] = sorted(
        current_zenn_csv, key=lambda x: x.title, reverse=True  # type: ignore
    )

    write_blog_article_to_csv(
        dto=WriteBlogArticleToCsvDto(
            file_path=Path(get_blog_article_csv_path(blog_service_name)),
            blog_articles=article_sorted,
        )
    )
