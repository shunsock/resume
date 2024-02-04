import requests

from resumer.infrastracture.fetch_zenn_rss.dto.fetch_zenn_rss_dto import FetchZennRssDto


def fetch_zenn_rss(dto: FetchZennRssDto) -> str:
    try:
        # Fetch the XML data
        response: requests.Response = requests.get(str(dto.url))
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"failed: fetching zenn rss; {e}")
