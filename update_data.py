from src.downloader.zenn import download_zenn_articles
from src.models.site import WEB_SITE_LIST
from src.service.supply_url import SiteSupply


def create_site_list() -> SiteSupply:
    return SiteSupply(WEB_SITE_LIST)


if __name__ == "__main__":
    sites: SiteSupply = create_site_list()
    download_zenn_articles(
        url=sites.get_url_by_name(name="zenn"), csv_path="src/techblog/data/zenn.csv"
    )
