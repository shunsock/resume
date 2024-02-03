from src.resume_builder.infrastracture.fetch_zenn_rss.dto.fetch_zenn_rss_dto import (
    FetchZennRssDto,
)
from src.resume_builder.infrastracture.fetch_zenn_rss.zenn_rss_repository import (
    fetch_zenn_rss,
)
from src.resume_builder.infrastracture.fetch_zenn_rss.zenn_rss_response_text_to_model import (
    zenn_rss_response_text_to_model,
)


def test_fetch_zenn_rss():
    # Arrange
    dto = FetchZennRssDto()

    # Act
    result = fetch_zenn_rss(dto)
    blog_articles = zenn_rss_response_text_to_model(result)
    print(blog_articles)

    # Assert
    assert blog_articles
