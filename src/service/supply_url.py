from typing import List

from src.models.site import Site


class SiteSupply:
    def __init__(self, sites_list: List[Site]):
        """
        Initialize SiteSupply object

        Parameters
        ======
        sites_list: List[Site] - list of Site objects

        Raises
        ======
        TypeError - if sites_list is not a list
        ValueError - if sites_list is empty
        """
        try:
            # Check if sites_list is a List
            if isinstance(sites_list, list) is False:
                raise TypeError("Sites list must be a list")

            # Check if sites_list is not empty
            # Check if sites_list object is a Site object
            for s in sites_list:
                if isinstance(s, Site) is False:
                    raise TypeError("Sites list must contain Site objects")
            self.sites = sites_list

            # Check if sites_list is not empty
            if len(self.sites) == 0:
                raise ValueError("Sites list must not be empty")
        except TypeError as te:
            raise TypeError(te)
        except ValueError as ve:
            raise ValueError(ve)

    def check_if_name_exists(self, name: str) -> bool:
        """
        Check if site with name exists

        Parameters
        ======
        name: str - site name

        Returns
        ======
        bool - True if site with name exists, False otherwise
        """
        if isinstance(name, str) is False:
            raise TypeError("Name must be a string")
        return any(site.name == name for site in self.sites)

    def check_if_url_exists(self, url: str) -> bool:
        """
        Check if site with url exists

        Parameters
        ======
        url: str - site url

        Returns
        ======
        bool - True if site with url exists, False otherwise
        """
        if isinstance(url, str) is False:
            raise TypeError("URL must be a string")
        return any(str(site.base_url) == url for site in self.sites)

    def get_url_by_name(self, name: str) -> str:
        """
        Get site url by name

        Parameters
        ======
        name: str - site name

        Returns
        ======
        str - site url

        Raises
        ======
        TypeError - if name is not a string
        ValueError - if site with name not found
        """
        if isinstance(name, str) is False:
            raise TypeError("Name must be a string")
        for site in self.sites:
            if site.name == name:
                return str(site.base_url)
        raise ValueError(f"Site with name {name} not found")
