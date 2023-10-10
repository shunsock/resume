from typing import List, Optional
from xml.etree import ElementTree

import requests
from pydantic import HttpUrl

from src.models.article import Article
from src.service import extract_new_article
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

        # -----------------------------
        # check if entry is valid
        # -----------------------------
        if item_title is None or item_link is None:
            continue

        # if type is not str, skip
        title_opt_str: Optional[str] = item_title.text
        link_opt_str: Optional[str] = item_link.text

        # -----------------------------
        # check if type is valid
        # -----------------------------
        title_type_not_str: bool = isinstance(title_opt_str, str) is False
        link_type_not_str: bool = isinstance(link_opt_str, str) is False
        if title_type_not_str or link_type_not_str:
            continue

        # NOTE: we can cast str to str
        # NOTE: to tell mypy that the type is not Optional[str]
        title_str: str = str(title_opt_str)
        link_str: str = str(link_opt_str)

        # -----------------------------
        # create Article Instance
        # -----------------------------
        article = Article(title=title_str, link=HttpUrl(link_str))
        articles.append(article)
    return articles


def update_zenn_articles(url: str, csv_path: str) -> None:
    current_articles: List[Article] = parse_zenn_rss_xml_to_article_class(url)
    saved_articles = ArticleSupply(read_articles_list_from_csv(csv_path))

    new_articles: List[Article] = extract_new_article.run(
        articles_downloaded=current_articles, articles_already_saved=saved_articles
    )

    if len(new_articles) == 0:
        print("新しい記事はありませんでした。")
    else:
        write_articles_to_csv(new_articles, "src/techblog/data/zenn.csv")
        print("記事を追加しました。")
