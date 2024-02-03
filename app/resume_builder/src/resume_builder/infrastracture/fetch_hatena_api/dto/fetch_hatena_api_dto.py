from pydantic import BaseModel, HttpUrl, StrictStr

from src.resume_builder.domain.api_config.hatena_api_config import HatenaApiConfig
from src.resume_builder.factory.api_config.hatena_api_config_factory import (
    create_hatena_api_config,
)


class FetchHatenaApiDto(BaseModel):
    name: StrictStr = "hatena blog"
    url: HttpUrl = HttpUrl("https://blog.hatena.ne.jp/")
    api_config: HatenaApiConfig = create_hatena_api_config()
