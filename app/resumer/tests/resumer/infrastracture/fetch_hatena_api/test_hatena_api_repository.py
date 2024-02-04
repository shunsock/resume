from resumer.infrastracture.fetch_hatena_api.dto.fetch_hatena_api_dto import (
    FetchHatenaApiDto,
)
from resumer.infrastracture.fetch_hatena_api.hatena_api_repository import (
    fetch_blog_entries,
)


def test_fetch_blog_entries():
    # Arrange
    dto = FetchHatenaApiDto()

    # Act
    result = fetch_blog_entries(dto)

    # Assert
    assert result
