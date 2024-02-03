from pydanic import HttpUrl, StrictStr

from src.resume_builder.domain.api_config.hatena_api_config import HatenaApiConfig
from src.resume_builder.domain.fetch_target_blog_service.fetch_target_blog_service_model import (
    FetchTargetBlogServiceModel,
)
from src.resume_builder.factory.api_config.hatena_api_config_factory import (
    create_hatena_api_config,
)


class HatenaApi(FetchTargetBlogServiceModel):
    name: StrictStr = "hatena blog"
    url: HttpUrl = "https://blog.hatena.ne.jp/"
    api_config: HatenaApiConfig = create_hatena_api_config()
