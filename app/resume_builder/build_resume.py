from resume_builder.hoge import hoge
from resume_builder.fuga.fuga import hello
from resume_builder.application.update_blog_article_csv.update_zenn_csv import update_zenn


def main():
    print("Updating blog article...")
    update_zenn()
    hoge()
    hello()
