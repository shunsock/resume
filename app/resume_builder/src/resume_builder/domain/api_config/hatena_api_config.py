from typing import Tuple

from pydantic import BaseModel, StrictStr


class HatenaApiConfig(BaseModel):
    """
    Hatena API config model

    Attributes:
        domain (StrictStr): URL of the blog
        user_name (StrictStr): username
        blog_name (StrictStr): blog name
        api_path (StrictStr): API path
        api_key (StrictStr): API key
    """

    # URL of the blog
    domain: StrictStr = "https://blog.hatena.ne.jp"
    user_name: StrictStr
    blog_name: StrictStr
    api_path: StrictStr = "atom/entry"

    # API key
    api_key: StrictStr

    def get_blog_entries_url(self) -> str:
        return f"{self.domain}/{self.user_name}/{self.blog_name}/{self.api_path}"

    def get_api_schema(self) -> Tuple[str, str]:
        return self.user_name, self.api_key
