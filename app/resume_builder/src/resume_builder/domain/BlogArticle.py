from pydantic import BaseModel, HttpUrl, StrictStr


class BlogArticle(BaseModel):
    """
    Article model

    Attributes:
        title (StrictStr): title of the article
        link (HttpUrl): link to the article
    """

    title: StrictStr
    link: HttpUrl
