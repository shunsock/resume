from zenn import parse_zenn_rss_xml_to_article_class
from models import Article, Site
from service.supply_url import SiteSupply
from service.article_handler import write_articles_to_csv
from typing import List


def create_site_list():
    SiteSupply(
        [
            Site("zenn", "https://zenn.dev/shundeveloper/feed")
        ]
    )
    return SiteSupply


if __name__ == "__main__":
    sites: List[Site] = create_site_list()
    zenn: List[Article] = parse_zenn_rss_xml_to_article_class(
        url=sites.get_url_by_name("zenn")
    )
    write_articles_to_csv(zenn, 'techblog/zenn.csv')
