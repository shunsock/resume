from src.models.article import Article
from src.service.supply_article import ArticleSupply


def article_supply_in_memory_mock():
    test_case = [
        Article(title="Test Article", link="https://www.testarticle.com/"),
        Article(title="Test Article2", link="https://www.testarticle2.com/"),
    ]
    articles = ArticleSupply(test_case)
    return articles


def test_construction_success():
    articles = article_supply_in_memory_mock()
    assert len(articles.articles) == 2
    assert articles.articles[0].title == "Test Article"
    assert articles.articles[1].title == "Test Article2"
    assert str(articles.articles[0].link) == "https://www.testarticle.com/"
    assert str(articles.articles[1].link) == "https://www.testarticle2.com/"

    for s in articles.articles:
        assert isinstance(s, Article) is True


def test_construction_failure_by_articles_list_is_not_list():
    try:
        ArticleSupply("Test Article")
        assert False
    except TypeError as e:
        print(e)
        assert True


def test_construction_failure_by_articles_list_is_empty():
    try:
        ArticleSupply([])
        assert False
    except ValueError as e:
        print(e)
        assert True


def test_check_if_title_exists():
    articles = article_supply_in_memory_mock()
    assert articles.check_if_title_exists("Test Article") is True
    assert articles.check_if_title_exists("Test Article2") is True
    assert articles.check_if_title_exists("Test Article3") is False


def test_check_if_title_exists_failure_by_title_is_not_string():
    articles = article_supply_in_memory_mock()
    try:
        articles.check_if_title_exists(123)
        assert False
    except TypeError:
        assert True


def test_check_if_link_exists():
    articles = article_supply_in_memory_mock()
    assert articles.check_if_link_exists("https://www.testarticle.com/") is True
    assert articles.check_if_link_exists("https://www.testarticle2.com/") is True
    assert articles.check_if_link_exists("https://www.testarticle3.com/") is False


def test_check_if_link_exists_failure_by_link_is_not_string():
    articles = article_supply_in_memory_mock()
    try:
        articles.check_if_link_exists(123)
        assert False
    except TypeError:
        assert True


def test_get_link_by_title():
    articles = article_supply_in_memory_mock()
    article = articles.get_link_by_title("Test Article")
    assert article == "https://www.testarticle.com/"

    article = articles.get_link_by_title("Test Article2")
    assert article == "https://www.testarticle2.com/"


def test_get_link_by_title_failure_by_title_is_not_string():
    articles = article_supply_in_memory_mock()
    try:
        articles.get_link_by_title(123)
        assert False
    except TypeError:
        assert True


def test_get_link_by_title_failure_by_title_is_not_found():
    articles = article_supply_in_memory_mock()
    try:
        articles.get_link_by_title("Test Article3")
        assert False
    except ValueError:
        assert True


def test_add_article_success():
    articles = article_supply_in_memory_mock()
    articles.add_article(
        Article(title="Test Article3", link="https://www.testarticle3.com/")
    )
    assert len(articles.articles) == 3
    print(articles.articles)
    assert articles.articles[0].title == "Test Article3"
    assert str(articles.articles[0].link) == "https://www.testarticle3.com/"


def test_add_article_failure_by_article_is_not_article():
    articles = article_supply_in_memory_mock()
    try:
        articles.add_article("Test Article3")
        assert False
    except TypeError:
        assert True
