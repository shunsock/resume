from resumer.application.update_blog_article_csv.update_hatena_csv import update_hatena
from resumer.application.update_blog_article_csv.update_zenn_csv import update_zenn


def update_blog_article_controller() -> None:
    update_zenn()
    update_hatena()


if __name__ == "__main__":
    update_blog_article_controller()
