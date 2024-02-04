from pathlib import Path
from typing import List

from resumer.domain.blog_article.blog_article_model import BlogArticleModel
from resumer.domain.blog_article.get_blog_article_csv_path import (
    get_blog_article_csv_path,
)
from resumer.domain.fetch_target_blog_service.hatena_api import HatenaApi
from resumer.infrastracture.fetch_hatena_api.dto.fetch_hatena_api_dto import (
    FetchHatenaApiDto,
)
from resumer.infrastracture.fetch_hatena_api.hatena_api_repository import (
    fetch_blog_entries,
)
from resumer.infrastracture.fetch_hatena_api.hatena_api_response_text_to_model import (
    hatena_api_response_text_to_model,
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


def update_hatena() -> None:
    """
    fetching zenn articles and update csv file
    Returns:

    """
    hatena_api: HatenaApi = HatenaApi()

    hatena_response_xml: str = fetch_blog_entries(dto=FetchHatenaApiDto())
    hatena_articles: List[BlogArticleModel] = hatena_api_response_text_to_model(
        api_response_text=hatena_response_xml
    )

    blog_service_name: str = hatena_api.name
    current_hatena_csv: List[BlogArticleModel] = read_blog_article_from_csv(
        dto=ReadBlogArticleFromCsvDto(
            blog_service_name=blog_service_name,
            file_path=get_blog_article_csv_path(blog_service_name),
        )
    )

    for article in hatena_articles:
        print("checking:", article.title)
        if article not in current_hatena_csv:
            print("new article found")
            print("adding:", article.title)
            current_hatena_csv.append(article)
        else:
            print("already exists")

    article_sorted: List[BlogArticleModel] = sorted(
        current_hatena_csv, key=lambda x: x.title, reverse=True  # type: ignore
    )

    write_blog_article_to_csv(
        dto=WriteBlogArticleToCsvDto(
            file_path=Path(get_blog_article_csv_path(blog_service_name)),
            blog_articles=article_sorted,
        )
    )
