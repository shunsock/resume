from typing import List, Optional
from xml.etree import ElementTree as ET

from pydantic import HttpUrl

from resumer.domain.blog_article.blog_article_model import BlogArticleModel
from resumer.infrastracture.helper.optional_str_to_str import optional_str_to_str


def hatena_api_response_text_to_model(api_response_text: str) -> List[BlogArticleModel]:
    """Converts the response from the Hatena API to a list of Entry models."""
    try:
        # Parse the XML data
        root = ET.fromstring(api_response_text)

        # Define the namespace
        namespaces = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", namespaces)
    except ET.ParseError as pe:  # Changed to catch XML-specific errors
        raise SystemExit(pe)

    articles: List[BlogArticleModel] = []  # Specify the type inside List
    while entries:
        entry = entries.pop()
        item_link = entry.find('atom:link[@rel="alternate"]', namespaces)
        item_title = entry.find("atom:title", namespaces)

        # Check if entry is valid
        if item_title is None or item_link is None:
            continue

        # Check if title and link are valid
        title: Optional[str] = item_title.text
        blog_article_title: str = optional_str_to_str(title)

        url: Optional[str] = item_link.get("href")
        blog_article_url: str = optional_str_to_str(url)

        if blog_article_title == "" or blog_article_url == "":
            continue

        blog_article_http_url: HttpUrl = HttpUrl(blog_article_url)

        # Directly create BlogArticleModel without casting since we now ensure all types are correct
        article = BlogArticleModel(
            blog_service_name="hatena_blog",
            title=blog_article_title,
            url=blog_article_http_url,
        )
        articles.append(article)
    return articles
