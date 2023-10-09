import os
from typing import List

from src.service.article_handler import read_articles_list_from_csv
from src.service.supply_article import ArticleSupply
from src.service import (
    supply_file_content,
    supply_path_list
)


def csv_to_md_table(file_path: str, site_name: str, tag_name: str) -> None:
    """
    Converts a csv file to a text file

    Parameters
    ======
    file_path: str

    Returns
    ======
    None

    Raises
    ======
    TypeError: if file_path is not a string
    FileNotFoundError: if file_path is not a valid file
    """
    if isinstance(file_path, str) is False:
        raise TypeError("file_path must be a string")
    if os.path.isfile(file_path) is False:
        raise FileNotFoundError("file_path must be a valid file")

    articles = ArticleSupply(read_articles_list_from_csv(file_path))
    with open("README.md", "a") as f:
        for article in articles.articles:
            title = "[" + article.title + "](" + str(article.link) + ")"
            row = "|" + site_name + "|" + tag_name + "|" + title + "|\n"
            f.write(row)


def build_techblog() -> None:
    with open("README.md", "a") as f:
        f.write("## Tech Blog\n")
        f.write("| Site Name | Tag      | Title       |\n")
        f.write("| ------    |------    | -----------|\n")

    # write articles to README.md
    csv_to_md_table(
        file_path="src/techblog/data/prtimes.csv",
        site_name="PR TIMES",
        tag_name="MLOps",
    )
    csv_to_md_table(
        file_path="src/techblog/data/zenn.csv", site_name="Zenn", tag_name="Web/Stats"
    )
    csv_to_md_table(
        file_path="src/techblog/data/toukei_no_mori.csv",
        site_name="Hello Statisicians!",
        tag_name="Machine Learning",
    )
    csv_to_md_table(
        file_path="src/techblog/data/hatena.csv",
        site_name="Hatena Blog",
        tag_name="Conference",
    )


def build_profile() -> None:
    """
    Builds the profile

    Parameters
    ======
    None

    Returns
    ======
    None
    """
    # write profile to README.md
    files_: List[str] = supply_path_list.get("src/profile/")
    files_ = sorted(files_)

    # we can not use name `file`
    # because it is a built-in function
    with open("README.md", "w") as readme:
        for file_ in files_:
            lines: List[str] = supply_file_content.get(file_)
            for line in lines:
                # print(line)
                readme.write(line)
            readme.write("\n")


if __name__ == "__main__":
    build_profile()
    build_techblog()
