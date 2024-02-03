import os


def get_blog_article_csv_path(blog_service_name: str) -> str:
    parent_dir = "data/blog_articles"
    return os.path.join(parent_dir, f"{blog_service_name}.csv")
