from src.models.site import Site
from src.service.supply_url import SiteSupply
from src.zenn import download_zenn_articles


def create_site_list() -> SiteSupply:
    return SiteSupply(
        sites_list=[
            Site(
                name="zenn",
                base_url="https://zenn.dev/shundeveloper/feed"
            )
        ]
    )


if __name__ == "__main__":
    sites: SiteSupply = create_site_list()
    download_zenn_articles(
        url=sites.get_url_by_name(name="zenn"),
        csv_path="src/techblog/data/zenn.csv"
    )
