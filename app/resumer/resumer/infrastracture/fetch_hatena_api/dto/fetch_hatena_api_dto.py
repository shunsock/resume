from pydantic import BaseModel, HttpUrl, StrictStr

from resumer.domain.api_config.hatena_api_config import HatenaApiConfig
from resumer.factory.api_config.hatena_api_config_factory import (
    create_hatena_api_config,
)


class FetchHatenaApiDto(BaseModel):
    name: StrictStr = "hatena blog"
    url: HttpUrl = HttpUrl(create_hatena_api_config().get_blog_entries_url())
    api_config: HatenaApiConfig = create_hatena_api_config()
