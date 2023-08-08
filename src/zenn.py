import xml.etree.ElementTree as ET
from typing import List, Optional
from xml.etree.ElementTree import Element

import requests

from src.models.article import Article


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
    return found_element.text.strip() if found_element is not None else None


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
        response = requests.get(url)
        xml_data = response.content
        tree = ET.fromstring(xml_data)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    articles: List = []
    for item in tree.findall(".//item"):
        article_data = {
            "title": get_element_text(item, "title"),
            "link": get_element_text(item, "link"),
        }
        article = Article(**article_data)
        articles.append(article)
    return articles
