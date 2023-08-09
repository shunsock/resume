import xml.etree.ElementTree as ET
from typing import List, Optional
from xml.etree.ElementTree import Element

import requests

from src.models.article import Article
from src.service.article_handler import (read_articles_list_from_csv,
                                         write_articles_to_csv)
from src.service.supply_article import ArticleSupply


def get_element_text(element: Element, tag_name: str) -> Optional[str]:
    """
    Get text from element

    Parameters
    ======
    element: Element - XML element
    tag_name: str - XML tag name

    Returns
    ======
    Optional[str] - text from element if element exists, None otherwise
    """
    found_element = element.find(tag_name)
    if isinstance(found_element, str):
        return found_element.text.strip()
    else:
        return None


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
    ======
    SystemExit - if request failed
    """
    try:
        response: requests.Response = requests.get(url)
        xml_data = response.content
        tree = ET.fromstring(xml_data)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    articles: List = []
    for item in tree.findall(".//item"):
        title = get_element_text(item, "title")
        link = get_element_text(item, "link")
        if isinstance(title, str) and isinstance(link, str):
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
