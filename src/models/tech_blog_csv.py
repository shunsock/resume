import os
from typing import List, Type

from pydantic import BaseModel, validator


class TechBlogCSV(BaseModel):
    file_path: str
    site_name: str
    tag_name: str

    @validator("file_path", pre=True, always=True)
    def validate_file_path(cls: Type[BaseModel], value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("file_path must be str")
        if not value.endswith(".csv"):
            raise ValueError(f"The file path {value} is not csv file")
        if not os.path.exists(value):
            raise ValueError(f"The file path {value} does not exist")
        return value


TECH_BLOG_CSV_LIST: List[TechBlogCSV] = [
    TechBlogCSV(
        file_path="src/techblog/data/prtimes.csv",
        site_name="PR TIMES",
        tag_name="MLOps",
    ),
    TechBlogCSV(
        file_path="src/techblog/data/zenn.csv", site_name="Zenn", tag_name="Web/Stats"
    ),
    TechBlogCSV(
        file_path="src/techblog/data/toukei_no_mori.csv",
        site_name="Hello Statisicians!",
        tag_name="Machine Learning",
    ),
    TechBlogCSV(
        file_path="src/techblog/data/hatena.csv",
        site_name="Hatena Blog",
        tag_name="Conference",
    ),
]
