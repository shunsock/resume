from typing import List, Type

from pydantic import BaseModel, ConfigDict, HttpUrl, field_validator


class Site(BaseModel):
    """
    Site model
    name: str - site name
    url: HttpUrl - site base url
    """

    name: str
    base_url: HttpUrl

    model_config = ConfigDict(extra="forbid")

    @field_validator("base_url")
    def check_base_url(cls: Type[BaseModel], v: HttpUrl) -> HttpUrl:
        assert str(v).startswith("https://"), "base_url must be https"
        return v


WEB_SITE_LIST: List[Site] = [
    Site(name="zenn", base_url=HttpUrl("https://zenn.dev/shundeveloper/feed")),
    Site(name="hatena", base_url=HttpUrl("https://blog.hatena.ne.jp/")),
]
