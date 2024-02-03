from resume_builder.application.update_blog_article_csv.update_zenn_csv import (
    update_zenn,
)


def update_blog_article_controller() -> None:
    update_zenn()


if __name__ == "__main__":
    update_blog_article_controller()
