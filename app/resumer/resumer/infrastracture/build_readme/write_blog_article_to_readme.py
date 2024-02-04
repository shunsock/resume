from resumer.infrastracture.build_readme.dto.write_blog_article_to_readme_dto import (
    WriteBlogArticleToReadmeDto,
)


def write_blog_article_to_readme(dto: WriteBlogArticleToReadmeDto) -> None:
    with open(dto.output_file_path, "a") as f:
        for article in dto.articles:
            title = "[" + article.title + "](" + str(article.url) + ")"
            row = "|" + article.blog_service_name + "|" + title + "\n"
            f.write(row)
