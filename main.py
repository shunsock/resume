from typing import List

from src.models.article import Article
from src.models.site import Site
from src.service.article_handler import (
    write_articles_to_csv,
    read_articles_list_from_csv
)
from src.service.supply_url import SiteSupply
from src.service.supply_article import ArticleSupply
from src.zenn import parse_zenn_rss_xml_to_article_class


def create_site_list():
    return SiteSupply(
        sites_list=[Site(name="zenn", base_url="https://zenn.dev/shundeveloper/feed")]
    )


def download_zenn_articles(
    url: str,
    csv_path: str
) -> None:
    current_article: List[Article] = parse_zenn_rss_xml_to_article_class(url)
    zenn = ArticleSupply(
        read_articles_list_from_csv(csv_path)
    )

    for article in current_article:
        is_new_link: bool = not zenn.check_if_link_exists(str(article.link))
        is_new_title: bool = not zenn.check_if_title_exists(article.title)
        if is_new_link and is_new_title:
            print(f"記事が存在しないため、記事を追加します。{article.title}")
            zenn.add_article(article)

    write_articles_to_csv(zenn.articles, "src/techblog/data/zenn.csv")


if __name__ == "__main__":
    sites: SiteSupply = create_site_list()
    download_zenn_articles(
        url=sites.get_url_by_name(name="zenn"),
        csv_path="src/techblog/data/zenn.csv"
    )
