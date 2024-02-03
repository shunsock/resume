from src.resume_builder.infrastracture.fetch_hatena_api.dto.fetch_hatena_api_dto import (
    FetchHatenaApiDto,
)
from src.resume_builder.infrastracture.fetch_hatena_api.hatena_api_repository import (
    fetch_blog_entries,
)
from src.resume_builder.infrastracture.fetch_hatena_api.hatena_api_response_text_to_model import (
    hatena_api_response_text_to_model,
)


def test_fetch_blog_entries():
    # Arrange
    dto = FetchHatenaApiDto()

    # Act
    result = fetch_blog_entries(dto)
    blog_articles = hatena_api_response_text_to_model(result)
    print(blog_articles)

    # Assert
    assert blog_articles
