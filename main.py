from src.zenn import parse_zenn_rss_xml_to_article_class
from src.models.article import Article
from src.models.site import Site
from src.service.supply_url import SiteSupply
from src.service.article_handler import write_articles_to_csv
from typing import List


def create_site_list():
    return SiteSupply(
        sites_list=[
            Site(name="zenn", base_url="https://zenn.dev/shundeveloper/feed")
        ]
    )


def download_zenn_articles(url: str) -> None:
    zenn: List[Article] = parse_zenn_rss_xml_to_article_class(
        url=url
    )
    write_articles_to_csv(zenn, 'src/techblog/data/zenn.csv')


if __name__ == "__main__":
    sites: SiteSupply = create_site_list()
    download_zenn_articles(sites.get_url_by_name(name="zenn"))
