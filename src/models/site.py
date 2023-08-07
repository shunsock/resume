from pydantic import BaseModel, HttpUrl


class Site(BaseModel):
    """
    Site model
    name: str - site name
    url: HttpUrl - site base url
    """

    name: str
    base_url: HttpUrl
