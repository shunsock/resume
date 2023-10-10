import os


def create_if_article_csv_not_exist(file_path: str) -> None:
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("title,link\n")
