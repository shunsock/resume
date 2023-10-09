from typing import List, Optional
from xml.etree import ElementTree

import requests

from src.models.article import Article
from src.service.article_handler import (
    read_articles_list_from_csv,
    write_articles_to_csv,
)
from src.service.supply_article import ArticleSupply


def parse_zenn_rss_xml_to_article_class(url: str) -> List[Article]:
    """
    Parse Zenn RSS XML to Article class

    Parameters
    ======
    url: str - RSS XML URL

    Returns
    ======
    List[Article] - list of Article class

    Raises

    SystemExit - if request failed
    """
    try:
        # Fetch the XML data
        response: requests.Response = requests.get(url)
        response.raise_for_status()
        xml_data = response.text
    except requests.exceptions.RequestException as syse:
        raise SystemExit(syse)

    try:
        # Parse the XML data into a dictionary
        root = ElementTree.fromstring(xml_data)
        channel = root.find("channel")
        if channel is not None:
            items = channel.findall("item")
        else:
            raise ValueError("channel is None")
    except ValueError as ve:
        raise SystemExit(ve)

    articles: List = []
    for item in items:
        title_ = item.find("title")
        link_ = item.find("link")
        if title_ is not None and link_ is not None:
            title: Optional[str] = title_.text
            link: Optional[str] = link_.text

            # MEMO
            # we have to type check because
            # sometimes the title and link are None
            title_type_str: bool = isinstance(title, str)
            link_type_str: bool = isinstance(link, str)
            if title_type_str and link_type_str:
                article = Article.model_validate({"title": title, "link": link})
                articles.append(article)
    return articles


def download_zenn_articles(url: str, csv_path: str) -> None:
    current_article: List[Article] = parse_zenn_rss_xml_to_article_class(url)
    zenn = ArticleSupply(read_articles_list_from_csv(csv_path))

    is_new_article_found: bool = False
    for article in current_article:
        is_new_link: bool = not zenn.check_if_link_exists(str(article.link))
        is_new_title: bool = not zenn.check_if_title_exists(article.title)
        if is_new_link and is_new_title:
            print(f"記事が存在しないため、記事を追加します。{article.title}")
            zenn.add_article(article)
            is_new_article_found = True

    if is_new_article_found is False:
        print("新しい記事はありませんでした。")

    write_articles_to_csv(zenn.articles, "src/techblog/data/zenn.csv")
