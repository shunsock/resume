from typing import List

from src.models.article import Article
from src.service.supply_article import ArticleSupply


def run(
    articles_downloaded: List[Article],
    articles_already_saved: ArticleSupply,
) -> List[Article]:
    """
    Extract new articles from downloaded articles.

    Parameters
    ----------
    articles_downloaded : List[Article]
        Downloaded articles.
    articles_saved : ArticleSupply
        Saved articles. (in src/techblog/data/csv)
    """
    new_articles: List[Article] = []
    for article in articles_downloaded:
        is_new_link: bool = not articles_already_saved.check_if_link_exists(
            str(article.link)
        )
        is_new_title: bool = not articles_already_saved.check_if_title_exists(
            article.title
        )
        if is_new_link and is_new_title:
            new_articles.append(article)
    return new_articles
