from resumer.infrastracture.fetch_zenn_rss.dto.fetch_zenn_rss_dto import FetchZennRssDto
from resumer.infrastracture.fetch_zenn_rss.zenn_rss_repository import fetch_zenn_rss


def test_fetch_zenn_rss():
    # Arrange
    dto = FetchZennRssDto()

    # Act
    result = fetch_zenn_rss(dto)

    # Assert
    assert result
