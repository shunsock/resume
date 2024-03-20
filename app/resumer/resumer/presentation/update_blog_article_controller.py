from resumer.application.update_blog_article_csv.update_hatena_csv import update_hatena
from resumer.application.update_blog_article_csv.update_zenn_csv import update_zenn
from resumer.application.update_readme.update_blog_article import update_blog_article
from resumer.application.update_readme.update_readme import update_readme


def update_blog_article_controller() -> None:
    update_zenn()
    update_hatena()


def update_readme_controller() -> None:
    # write mode to README.md
    update_readme()

    # append blog data
    update_blog_article()
