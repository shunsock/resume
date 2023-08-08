from src.models.article import Article
from src.service.supply_article import ArticleSupply


def article_supply_in_memory_mock():
    test_case = [
        Article(title="Test Article", link="http://www.testarticle.com/"),
        Article(title="Test Article2", link="http://www.testarticle2.com/"),
    ]
    article_supply = ArticleSupply(test_case)
    return article_supply


def test_construction_success():
    article_supply = article_supply_in_memory_mock()
    assert len(article_supply.articles) == 2
    assert article_supply.articles[0].title == "Test Article"
    assert article_supply.articles[1].title == "Test Article2"
    assert str(article_supply.articles[0].link) == "http://www.testarticle.com/"
    assert str(article_supply.articles[1].link) == "http://www.testarticle2.com/"

    for s in article_supply.articles:
        assert isinstance(s, Article) is True


def test_construction_failure_by_articles_list_is_not_list():
    try:
        article_supply = ArticleSupply("Test Article")
        print(article_supply)
        assert False
    except TypeError as e:
        print(e)
        assert True


def test_construction_failure_by_articles_list_is_empty():
    try:
        article_supply = ArticleSupply([])
        print(article_supply)
        assert False
    except ValueError as e:
        print(e)
        assert True


def test_check_if_title_exists():
    article_supply = article_supply_in_memory_mock()
    assert article_supply.check_if_title_exists("Test Article") is True
    assert article_supply.check_if_title_exists("Test Article2") is True
    assert article_supply.check_if_title_exists("Test Article3") is False


def test_check_if_title_exists_failure_by_title_is_not_string():
    article_supply = article_supply_in_memory_mock()
    try:
        article_supply.check_if_title_exists(123)
        assert False
    except TypeError:
        assert True


def test_check_if_link_exists():
    article_supply = article_supply_in_memory_mock()
    assert article_supply.check_if_link_exists("http://www.testarticle.com/") is True
    assert article_supply.check_if_link_exists("http://www.testarticle2.com/") is True
    assert article_supply.check_if_link_exists("http://www.testarticle3.com/") is False


def test_check_if_link_exists_failure_by_link_is_not_string():
    article_supply = article_supply_in_memory_mock()
    try:
        article_supply.check_if_link_exists(123)
        assert False
    except TypeError:
        assert True


def test_get_link_by_title():
    article_supply = article_supply_in_memory_mock()
    article = article_supply.get_link_by_title("Test Article")
    assert article == "http://www.testarticle.com/"

    article = article_supply.get_link_by_title("Test Article2")
    assert article == "http://www.testarticle2.com/"


def test_get_link_by_title_failure_by_title_is_not_string():
    article_supply = article_supply_in_memory_mock()
    try:
        article_supply.get_link_by_title(123)
        assert False
    except TypeError:
        assert True


def test_get_link_by_title_failure_by_title_is_not_found():
    article_supply = article_supply_in_memory_mock()
    try:
        article_supply.get_link_by_title("Test Article3")
        assert False
    except ValueError:
        assert True
