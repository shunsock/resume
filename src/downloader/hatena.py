from typing import List, Optional, Tuple
from xml.etree import ElementTree as ET

import requests
from dotenv import dotenv_values
from pydantic import HttpUrl

from src.models.article import Article
from src.service import extract_new_article
from src.service.article_handler import (read_articles_list_from_csv,
                                         write_articles_to_csv)
from src.service.supply_article import ArticleSupply


def get_rss_from_server() -> str:
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
        return xml_data
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)


def parse_hatena_rss_xml_to_article_class() -> List[Article]:
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

    # ----------------------------------
    # dump entries to Article class List
    # ----------------------------------
    articles: List = []
    while len(entries) > 0:
        entry = entries.pop()
        item_link = entry.find('atom:link[@rel="alternate"]', namespaces)
        item_title = entry.find("atom:title", namespaces)

        # -----------------------------
        # check if entry is valid
        # -----------------------------

        # if object not found, skip
        if item_title is None or item_link is None:
            continue

        # NOTE: existance of object is preserved by previous statement
        title_opt_str: Optional[str] = item_title.text
        link_opt_str: Optional[str] = item_link.get("href")

        # -----------------------------
        # check if type is valid
        # -----------------------------

        # if type is not str, skip
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


def update_hatena_articles(csv_path: str) -> None:
    current_articles = parse_hatena_rss_xml_to_article_class()
    saved_articles = ArticleSupply(read_articles_list_from_csv(csv_path))
    new_articles: List[Article] = extract_new_article.run(
        articles_downloaded=current_articles,
        articles_already_saved=saved_articles,
    )

    if len(new_articles) == 0:
        print("新しい記事はありませんでした。")
    else:
        write_articles_to_csv(new_articles, csv_path)
        print("記事を追加しました。")
