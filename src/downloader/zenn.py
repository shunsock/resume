from typing import List, Optional
from xml.etree import ElementTree

import requests
from pydantic import HttpUrl

from src.models.article import Article
from src.service.article_handler import (read_articles_list_from_csv,
                                         write_articles_to_csv)
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
    while len(items) > 0:
        item = items.pop()

        item_title = item.find("title")
        item_link = item.find("link")
        if item_title is None or item_link is None:
            continue

        title_opt_str: Optional[str] = item_title.text
        link_opt_str: Optional[str] = item_link.text

        # MEMO
        # we have to type check because
        # sometimes the title and link are None
        title_type_not_str: bool = isinstance(title_opt_str, str) is False
        link_type_not_str: bool = isinstance(link_opt_str, str) is False
        if title_type_not_str or link_type_not_str:
            continue

        title_str: str = str(title_opt_str)
        link_str: str = str(link_opt_str)
        article = Article(title=title_str, link=HttpUrl(link_str))
        articles.append(article)
    return articles


def update_zenn_articles(url: str, csv_path: str) -> None:
    current_article: List[Article] = parse_zenn_rss_xml_to_article_class(url)
    zenn = ArticleSupply(read_articles_list_from_csv(csv_path))

    new_articles: List[Article] = []
    is_new_article_found: bool = False
    for article in current_article:
        is_new_link: bool = not zenn.check_if_link_exists(str(article.link))
        is_new_title: bool = not zenn.check_if_title_exists(article.title)
        if is_new_link and is_new_title:
            print(f"記事が存在しないため、記事を追加します。{article.title}")
            new_articles.append(article)
            is_new_article_found = True

    if is_new_article_found is False:
        print("新しい記事はありませんでした。")
    else:
        write_articles_to_csv(new_articles, "src/techblog/data/zenn.csv")
        print("記事を追加しました。")
