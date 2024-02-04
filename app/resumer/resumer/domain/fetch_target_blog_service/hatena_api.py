from pydantic import HttpUrl, StrictStr

from resumer.domain.api_config.hatena_api_config import HatenaApiConfig
from resumer.domain.fetch_target_blog_service.fetch_target_blog_service_model import (
    FetchTargetBlogServiceModel,
)
from resumer.factory.api_config.hatena_api_config_factory import (
    create_hatena_api_config,
)


class HatenaApi(FetchTargetBlogServiceModel):
    name: StrictStr
    url: HttpUrl
    api_config: HatenaApiConfig = create_hatena_api_config()

    def __init__(self) -> None:
        super().__init__(name=StrictStr("hatena_blog"), url=HttpUrl("https://blog.hatena.ne.jp/"))
