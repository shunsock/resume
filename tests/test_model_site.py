from pydantic import ValidationError

from src.models.site import Site


def test_construction_success():
    url = "https://www.testsite.com/"
    site = Site(name="Test Site", base_url=url)
    assert site.name == "Test Site"
    assert str(site.base_url) == url


def test_construction_failure_by_name():
    try:
        Site(
            name=123,
            base_url="https://www.testsite.com/",
        )
        assert False
    except ValidationError:
        assert True


def test_construction_failure_by_url_is_invalid():
    try:
        Site(
            name="Test Site",
            base_url="hogehoge",
        )
        assert False
    except ValidationError:
        assert True


def test_construction_failure_by_url_is_int():
    try:
        Site(
            name="Test Site",
            base_url=123,
        )
        assert False
    except ValidationError:
        assert True
