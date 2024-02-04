import os


def get_blog_article_csv_path(blog_service_name: str) -> str:
    parent_dir = "resumer/data/blog_article"
    return os.path.join(parent_dir, f"{blog_service_name}.csv")
