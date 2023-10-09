from src.models.site import Site
from src.service.supply_url import SiteSupply


def site_supply_in_memory_mock():
    test_case = [
        Site(name="Test Site", base_url="https://www.testsite.com/"),
        Site(name="Test Site2", base_url="https://www.testsite2.com/"),
    ]
    site_supply = SiteSupply(test_case)
    return site_supply


def test_construction_success():
    site_supply = site_supply_in_memory_mock()
    assert len(site_supply.sites) == 2
    assert site_supply.sites[0].name == "Test Site"
    assert site_supply.sites[1].name == "Test Site2"
    assert str(site_supply.sites[0].base_url) == "https://www.testsite.com/"
    assert str(site_supply.sites[1].base_url) == "https://www.testsite2.com/"

    for s in site_supply.sites:
        assert isinstance(s, Site) is True


def test_construction_failure_by_sites_list_is_not_list():
    try:
        site_supply = SiteSupply("Test Site")
        assert False
    except TypeError:
        assert True


def test_construction_failure_by_sites_list_is_empty():
    try:
        site_supply = SiteSupply([])
        assert False
    except ValueError:
        assert True


def test_check_if_name_exists():
    site_supply = site_supply_in_memory_mock()
    assert site_supply.check_if_name_exists("Test Site") is True
    assert site_supply.check_if_name_exists("Test Site2") is True
    assert site_supply.check_if_name_exists("Test Site3") is False


def test_check_if_name_exists_failure_by_name_is_not_string():
    site_supply = site_supply_in_memory_mock()
    try:
        site_supply.check_if_name_exists(123)
        assert False
    except TypeError:
        assert True


def test_check_if_url_exists():
    site_supply = site_supply_in_memory_mock()
    assert site_supply.check_if_url_exists("https://www.testsite.com/") is True
    assert site_supply.check_if_url_exists("https://www.testsite2.com/") is True
    assert site_supply.check_if_url_exists("https://www.testsite3.com/") is False


def test_check_if_url_exists_failure_by_url_is_not_string():
    site_supply = site_supply_in_memory_mock()
    try:
        site_supply.check_if_url_exists(123)
        assert False
    except TypeError:
        assert True


def test_get_url_by_name():
    site_supply = site_supply_in_memory_mock()
    site = site_supply.get_url_by_name("Test Site")
    assert site == "https://www.testsite.com/"

    site = site_supply.get_url_by_name("Test Site2")
    assert site == "https://www.testsite2.com/"


def test_get_url_by_name_failure_by_name_is_not_string():
    site_supply = site_supply_in_memory_mock()
    try:
        site_supply.get_url_by_name(123)
        assert False
    except TypeError:
        assert True


def test_get_url_by_name_failure_by_name_is_not_found():
    site_supply = site_supply_in_memory_mock()
    try:
        site_supply.get_url_by_name("Test Site3")
        assert False
    except ValueError:
        assert True
