from resumer.domain.readme.readme import Readme
from resumer.infrastracture.build_readme.dto.write_blog_article_to_readme_dto import (
    WriteBlogArticleToReadmeDto,
)
from resumer.infrastracture.build_readme.write_blog_article_to_readme import (
    write_blog_article_to_readme,
)
from resumer.infrastracture.read_blog_article_csv.dto.read_blog_article_csv_dto import (
    ReadBlogArticleFromCsvDto,
)
from resumer.infrastracture.read_blog_article_csv.read_blog_article_from_csv import (
    read_blog_article_from_csv,
)
from typing import List


def update_blog_article() -> None:
    readme: Readme = Readme()

    # TODO: think method to handle blog name
    file_paths: List[ReadBlogArticleFromCsvDto] = [
        ReadBlogArticleFromCsvDto(
            file_path="resumer/data/blog_article/hatena_blog.csv",
            blog_service_name="hatena_blog",
        ),
        ReadBlogArticleFromCsvDto(
            file_path="resumer/data/blog_article/zenn.csv",
            blog_service_name="zenn",
        ),
        ReadBlogArticleFromCsvDto(
            file_path="resumer/data/blog_article/prtimes_tech_blog.csv",
            blog_service_name="prtimes_tech_blog",
        ),
        ReadBlogArticleFromCsvDto(
            file_path="resumer/data/blog_article/toukei_no_mori.csv",
            blog_service_name="toukei_no_mori",
        ),
    ]


    with open(str(readme.output_file_path), "a") as f:
        f.write("## Tech Blog\n")
        f.write("| Site Name | Title       |\n")
        f.write("| ------    | -----------|\n")

    for file_path in file_paths:
        articles = read_blog_article_from_csv(file_path)

        write_blog_article_to_readme(
            dto=WriteBlogArticleToReadmeDto(
                output_file_path=str(readme.output_file_path),
                articles=articles,
            )
        )
