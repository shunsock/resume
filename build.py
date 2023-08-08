from typing import List
from src.service.article_handler import read_articles_list_from_csv
from src.service.supply_article import ArticleSupply
import os


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
        raise TypeError('file_path must be a string')
    if os.path.isfile(file_path) is False:
        raise FileNotFoundError('file_path must be a valid file')

    articles = ArticleSupply(
        read_articles_list_from_csv(file_path)
    )
    with open("README.md", "a") as f:
        for article in articles.articles:
            title = "[" + article.title+"]("+str(article.link)+")"
            row = "|" + site_name + "|" + tag_name + "|" + title + "|\n"
            f.write(row)


def build_techblog() -> None:
    with open("README.md", "a") as f:
        f.write("## Tech Blog\n")
        f.write("| Site Name | Tag      | Title       |\n")
        f.write("| ------    |------    | -----------|\n")

    # write articles to README.md
    csv_to_md_table(
        file_path='src/techblog/data/prtimes.csv',
        site_name='PR TIMES',
        tag_name='MLOps'
    )
    csv_to_md_table(
        file_path='src/techblog/data/zenn.csv',
        site_name='Zenn',
        tag_name='Web \n ML&Stats'
    )
    csv_to_md_table(
        file_path='src/techblog/data/toukei_no_mori.csv',
        site_name='Hello Statisicians!',
        tag_name='ML&Stats'
    )
    csv_to_md_table(
        file_path='src/techblog/data/hatena.csv',
        site_name='Hatena Blog',
        tag_name='Conference'
    )


def get_path_list(directory: str) -> List[str]:
    """
        Returns a list of all .txt files in a directory

        Parameters
        ======
        directory: str

        Returns
        ======
        List[str]

        Raises
        ======
        TypeError: if directory is not a string
        NotADirectoryError: if directory is not a valid directory
    """
    if isinstance(directory, str) is False:
        raise TypeError('directory must be a string')
    if os.path.isdir(directory) is False:
        raise NotADirectoryError('directory must be a valid directory')

    txt_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
    return txt_files


def get_file_contents(file_path: str) -> List[str]:
    """
        Returns the contents of a file

        Parameters
        ======
        file_path: str

        Returns
        ======
        str

        Raises
        ======
        TypeError: if file_path is not a string
        FileNotFoundError: if file_path is not a valid file
    """
    if isinstance(file_path, str) is False:
        raise TypeError('file_path must be a string')
    if os.path.isfile(file_path) is False:
        raise FileNotFoundError('file_path must be a valid file')

    with open(file_path, 'r') as f:
        return f.readlines()


def build_profile() -> None:
    # write profile to README.md
    files: List[str] = get_path_list('src/profile/')
    with open('README.md', 'w') as readme:
        for f in files:
            lines: List[str] = sorted(get_file_contents(f))
            for line in lines:
                # print(line)
                readme.write(line + '\n')


if __name__ == '__main__':
    build_profile()
    build_techblog()
