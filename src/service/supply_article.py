from typing import List

from src.models.article import Article


class ArticleSupply:
    """
        ArticleSupply class

        Properties
        ======
        articles: List[Article] - list of Article objects
    """

    def __init__(self, articles_list: List[Article]):
        """
        Initialize ArticleSupply object

        Parameters
        ======
        articles_list: List[Article] - list of Article objects

        Raises
        ======
        TypeError - if articles_list is not a list
        ValueError - if articles_list is empty
        """
        try:
            # Check if articles_list is a List
            if isinstance(articles_list, list) is False:
                raise TypeError("Articles list must be a list")

            # Check if articles_list is not empty
            # Check if articles_list object is a Article object
            for s in articles_list:
                if isinstance(s, Article) is False:
                    raise TypeError("Articles list must contain Article objects")
            self.articles = articles_list

            # Check if articles_list is not empty
            if len(self.articles) == 0:
                raise ValueError("Articles list must not be empty")

        except TypeError as te:
            raise TypeError(te)
        except ValueError as ve:
            raise ValueError(ve)

    def check_if_title_exists(self, title: str) -> bool:
        """
        Check if article with title exists

        Parameters
        ======
        title: str - article title

        Returns
        ======
        bool - True if article with title exists, False otherwise
        """
        if isinstance(title, str) is False:
            raise TypeError("title must be a string")
        return any(article.title == title for article in self.articles)

    def check_if_link_exists(self, link: str) -> bool:
        """
        Check if article with link exists

        Parameters
        ======
        link: str - article link

        Returns
        ======
        bool - True if article with link exists, False otherwise
        """
        if isinstance(link, str) is False:
            raise TypeError("link must be a string")
        return any(str(article.link) == link for article in self.articles)

    def get_link_by_title(self, title: str) -> str:
        """
        Get article link by title

        Parameters
        ======
        title: str - article title

        Returns
        ======
        str - article link

        Raises
        ======
        TypeError - if title is not a string
        ValueError - if article with title not found
        """
        if isinstance(title, str) is False:
            raise TypeError("title must be a string")
        for article in self.articles:
            if article.title == title:
                return str(article.link)
        raise ValueError(f"Article with title {title} not found")

    def add_article(self, new_article: Article) -> None:
        """
        Add article to articles list

        Parameters
        ======
        new_article: Article - Article object

        Returns
        ======
        None

        Raises
        ======
        TypeError - if new_article is not a Article object
        ValueError - if new_article already exists
        """
        if isinstance(new_article, Article) is False:
            raise TypeError(
                "new_article must be a Article object"
            )
        if self.check_if_title_exists(new_article.title):
            raise ValueError(
                f"Article with title {new_article.title} already exists"
            )
        if self.check_if_link_exists(str(new_article.link)):
            raise ValueError(
                f"Article with link {new_article.link} already exists"
            )
        self.articles.insert(0, new_article)
