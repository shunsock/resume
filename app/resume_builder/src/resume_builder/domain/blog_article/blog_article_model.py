from pydantic import BaseModel, HttpUrl, StrictStr


class BlogArticleModel(BaseModel):
    """
    Blog article model
    title: StrictStr - article title
    url: StrictStr - article URL
    """

    title: StrictStr
    url: HttpUrl
