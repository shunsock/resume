from typing import Type

from pydantic import BaseModel, ConfigDict, HttpUrl, field_validator


class Article(BaseModel):
    """
    Article model

    Attributes:
        title (str): title of the article
        link (UrlStr): link to the article
    """

    title: str
    link: HttpUrl

    model_config = ConfigDict(extra="forbid")

    @field_validator("link")
    def check_link(cls: Type[BaseModel], v: HttpUrl) -> HttpUrl:
        assert str(v).startswith("https://"), "link must be https"
        return v
