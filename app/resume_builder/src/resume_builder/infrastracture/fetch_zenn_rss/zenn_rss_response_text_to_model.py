from typing import List, Optional
from xml.etree import ElementTree

from pydantic import HttpUrl

from src.resume_builder.domain.blog_article.blog_article_model import BlogArticleModel
from src.resume_builder.infrastracture.helper.optional_str_to_str import (
    optional_str_to_str,
)


def zenn_rss_response_text_to_model(text: str) -> List[BlogArticleModel]:
    """Converts a Zenn RSS response text to a list of BlogArticle."""
    try:
        # Parse the XML data into a dictionary
        root = ElementTree.fromstring(text)
        channel = root.find("channel")
        if channel is not None:
            items = channel.findall("item")
        else:
            raise ValueError("channel is None")
    except ValueError as ve:
        raise SystemExit(ve)

    articles: List[BlogArticleModel] = []
    while len(items) > 0:
        item = items.pop()
        item_title = item.find("title")
        item_link = item.find("link")

        # -----------------------------
        # check if entry is valid
        # -----------------------------
        if item_title is None or item_link is None:
            continue

        title: Optional[str] = item_title.text
        blog_article_title: str = optional_str_to_str(title)

        url: Optional[str] = item_link.text
        blog_article_url: str = optional_str_to_str(url)

        if blog_article_title == "" or blog_article_url == "":
            continue

        blog_article_http_url: HttpUrl = HttpUrl(blog_article_url)

        article = BlogArticleModel(
            blog_service_name="zenn",
            title=blog_article_title,
            url=blog_article_http_url,
        )
        articles.append(article)
    return articles
