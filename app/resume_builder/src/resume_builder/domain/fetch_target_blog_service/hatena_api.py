from pydanic import HttpUrl, StrictStr

from src.resume_builder.domain.fetch_target_blog_service.fetch_target_blog_service_model import (
    FetchTargetBlogServiceModel,
)


class HatenaBlog(FetchTargetBlogServiceModel):
    name: StrictStr = "hatena"
    url: HttpUrl = "https://blog.hatena.ne.jp/"
