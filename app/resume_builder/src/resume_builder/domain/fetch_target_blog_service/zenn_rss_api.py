from pydanic import HttpUrl, StrictStr

from src.resume_builder.domain.fetch_target_blog_service.fetch_target_blog_service_model import (
    FetchTargetBlogServiceModel,
)


class ZennApi(FetchTargetBlogServiceModel):
    name: StrictStr = "zenn"
    url: HttpUrl = "https://zenn.dev/shundeveloper/feed"
