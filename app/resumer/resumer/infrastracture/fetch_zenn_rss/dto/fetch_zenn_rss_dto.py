from pydantic import BaseModel, HttpUrl


class FetchZennRssDto(BaseModel):
    """
    Fetch Zenn RSS Dto
    url: HttpUrl - Zenn RSS URL
    """

    url: HttpUrl = HttpUrl("https://zenn.dev/shundeveloper/feed")
