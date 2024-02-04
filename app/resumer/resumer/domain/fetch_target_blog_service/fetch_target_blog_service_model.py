from pydantic import BaseModel, HttpUrl, StrictStr


class FetchTargetBlogServiceModel(BaseModel):
    """
    Site model
    name: StrictStr - site name
    url: HttpUrl - site base url
    """

    name: StrictStr
    url: HttpUrl
