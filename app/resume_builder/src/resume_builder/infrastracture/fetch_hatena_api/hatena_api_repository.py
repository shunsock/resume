import requests

from src.resume_builder.infrastracture.fetch_hatena_api.dto.fetch_hatena_api_dto import (
    FetchHatenaApiDto,
)


def fetch_blog_entries(dto: FetchHatenaApiDto) -> str:
    """
    Fetch blog entries
    Parameters:
        dto: FetchHatenaApiDto - Hatena API DTO

    Returns:
        str: blog entries
    """
    try:
        response: requests.Response = requests.get(
            str(dto.url), auth=dto.api_config.get_api_schema()
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise e
