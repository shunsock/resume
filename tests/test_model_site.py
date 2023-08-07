from pydantic import ValidationError

from src.models.site import Site


def test_construction_success():
    url = "http://www.testsite.com/"
    site = Site(name="Test Site", base_url=url)
    assert site.name == "Test Site"
    assert str(site.base_url) == url


def test_construction_failure_by_name():
    try:
        site = Site(
            name=123,
            base_url="http://www.testsite.com/",
        )
        assert False
    except ValidationError:
        assert True


def test_construction_failure_by_url_is_invalid():
    try:
        site = Site(
            name="Test Site",
            base_url="hogehoge",
        )
        assert False
    except ValidationError:
        assert True


def test_construction_failure_by_url_is_int():
    try:
        site = Site(
            name="Test Site",
            base_url=123,
        )
        assert False
    except ValidationError:
        assert True
