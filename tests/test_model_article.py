from pydantic import ValidationError

from src.models.article import Article


def test_model_article_success():
    try:
        target_link = "https://zenn.dev/shundeveloper/articles/86e3cda89492d4"
        article = Article(title="title", link=target_link)

        # assert if the article is constructed correctly
        assert article.title == "title"
        assert str(article.link) == target_link  # convert to string to compare
    except ValidationError as ve:
        # if inputs are invalid, raise ValidationError
        raise ValidationError(ve)


def test_model_article_fail_if_link_invalid() -> None:
    """
    Test if the article model raises ValidationError
    when the link is invalid
    """
    try:
        # warnings on editor are ok.
        # this is just to test if the model raises ValidationError
        target_link = "http\\zenn.dev/shundeveloper/articles/86e3cda89492d4"
        Article(title="title", link=target_link)
    except ValidationError:
        assert True


def test_mode_article_fail_if_link_is_not_https() -> None:
    """
    Test if the article model raises ValidationError
    when the link is not https
    """
    try:
        target_link = "http://zenn.dev/shundeveloper/articles/86e3cda89492d4"
        Article(title="title", link=target_link)
    except ValidationError:
        assert True
