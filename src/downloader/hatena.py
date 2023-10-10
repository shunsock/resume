from typing import List, Optional, Tuple
from xml.etree import ElementTree as ET

import requests
from dotenv import dotenv_values
from pydantic import HttpUrl

from src.models.article import Article
from src.service.article_handler import (read_articles_list_from_csv,
                                         write_articles_to_csv)
from src.service.supply_article import ArticleSupply


def parse_hatena_rss_xml_to_article_class(url: str) -> List[Article]:
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
    # read .env file
    config = dotenv_values(".env")

    if config["HATENA_USER_NAME"] is None:
        raise SystemExit("HATENA_USER_NAME is not defined")
    if config["HATENA_BLOG_NAME"] is None:
        raise SystemExit("HATENA_BLOG_NAME is not defined")
    if config["HATENA_API_KEY"] is None:
        raise SystemExit("HATENA_API_KEY is not defined")
    user_name: str = config["HATENA_USER_NAME"]
    blog_name: str = config["HATENA_BLOG_NAME"]
    api_key: str = config["HATENA_API_KEY"]

    # create http request
    blog_entries_url = f"https://blog.hatena.ne.jp/{user_name}/{blog_name}/atom/entry"
    user_pass_tuple: Tuple[str, str] = (user_name, api_key)
    try:
        # Fetch the XML data
        response: requests.Response = requests.get(
            blog_entries_url, auth=user_pass_tuple
        )
        response.raise_for_status()
        xml_data = response.text
    except requests.exceptions.RequestException as syse:
        raise SystemExit(syse)

    try:
        # Parse the XML data
        root = ET.fromstring(xml_data)

        # Define the namespace
        namespaces = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", namespaces)
    except ValueError as ve:
        raise SystemExit(ve)

    articles: List = []
    while len(entries) > 0:
        entry = entries.pop()
        item_link = entry.find('atom:link[@rel="alternate"]', namespaces)
        item_title = entry.find("atom:title", namespaces)

        if item_title is None or item_link is None:
            continue

        title_opt_str: Optional[str] = item_title.text
        link_opt_str: Optional[str] = item_link.get("href")

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


def update_hatena_articles(url: str, csv_path: str) -> None:
    current_article: List[Article] = parse_hatena_rss_xml_to_article_class(url)
    zenn = ArticleSupply(read_articles_list_from_csv(csv_path))

    new_articles: List[Article] = []
    is_new_article_found: bool = False
    for article in current_article:
        is_new_link: bool = not zenn.check_if_link_exists(str(article.link))
        is_new_title: bool = not zenn.check_if_title_exists(article.title)
        if is_new_link and is_new_title:
            new_articles.append(article)
            is_new_article_found = True

    if is_new_article_found is False:
        print("新しい記事はありませんでした。")
    else:
        write_articles_to_csv(new_articles, csv_path)
        print("記事を追加しました。")
