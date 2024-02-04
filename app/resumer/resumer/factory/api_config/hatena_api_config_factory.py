from typing import Dict, Optional

from dotenv import dotenv_values

from resumer.domain.api_config.hatena_api_config import HatenaApiConfig
from resumer.infrastracture.helper.optional_str_to_str import optional_str_to_str


def create_hatena_api_config() -> HatenaApiConfig:
    config: Dict[str, Optional[str]] = dotenv_values(".env")

    user_name: Optional[str] = config["HATENA_USER_NAME"]
    user_name_str: str = optional_str_to_str(user_name)
    user_name_exist: bool = user_name_str != ""

    blog_name: Optional[str] = config["HATENA_BLOG_NAME"]
    blog_name_str: str = optional_str_to_str(blog_name)
    blog_name_exist: bool = blog_name_str != ""

    api_key: Optional[str] = config["HATENA_API_KEY"]
    api_key_str: str = optional_str_to_str(api_key)
    api_key_exist: bool = api_key_str != ""

    if not user_name_exist or not blog_name_exist or not api_key_exist:
        raise ValueError("you have to set .env correctly")

    return HatenaApiConfig(
        user_name=user_name_str, blog_name=blog_name_str, api_key=api_key_str
    )
