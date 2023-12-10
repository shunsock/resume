from typing import List

from src.downloader.hatena import update_hatena_articles
from src.downloader.zenn import update_zenn_articles
from src.models.article import Article
from src.models.site import WEB_SITE_LIST
from src.service.article_handler import write_articles_to_csv
from src.service.supply_url import SiteSupply


def create_site_list() -> SiteSupply:
    return SiteSupply(WEB_SITE_LIST)


def add_new_articles_to_csv(new_articles: List[Article], csv_path: str) -> None:
    write_articles_to_csv(new_articles, csv_path)


if __name__ == "__main__":
    sites: SiteSupply = create_site_list()
    update_zenn_articles(
        url=sites.get_url_by_name(name="zenn"), csv_path="src/techblog/data/zenn.csv"
    )
    update_hatena_articles(
        csv_path="src/techblog/data/hatena.csv",
    )
