from pydantic import HttpUrl, StrictStr

from resumer.domain.fetch_target_blog_service.fetch_target_blog_service_model import (
    FetchTargetBlogServiceModel,
)


class ZennRssApi(FetchTargetBlogServiceModel):
    name: StrictStr = "zenn"
    url: HttpUrl = "https://zenn.dev/shundeveloper/feed"
