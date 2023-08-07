from pydantic import BaseModel, HttpUrl


class Article(BaseModel):
    title: str
    link: HttpUrl
