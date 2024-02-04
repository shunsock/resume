import os

from resumer.domain.blog_article.blog_article_model import BlogArticleModel
from resumer.infrastracture.build_readme.dto.write_blog_article_to_readme_dto import (
    WriteBlogArticleToReadmeDto,
)
from resumer.infrastracture.build_readme.write_blog_article_to_readme import (
    write_blog_article_to_readme,
)


def test_write_blog_article_to_readme():
    output_file_path = "resumer/data/test/infrastracture/build_resume/README.md"
    # given
    dto = WriteBlogArticleToReadmeDto(
        output_file_path=output_file_path,
        articles=[
            BlogArticleModel(
                title="Fastly Yamagoya 2023に参加しました！",
                url="https://shundeveloper.hatenablog.com/entry/fastly_yamagoya2023",
                blog_service_name="hatena_blog",
            )
        ],
    )
    # when
    write_blog_article_to_readme(dto)
    # then
    with open(output_file_path, "r") as f:
        contents = f.readlines()
        assert (
            contents[-1]
            == "|hatena_blog|[Fastly Yamagoya 2023に参加しました！](https://shundeveloper.hatenablog.com/entry/fastly_yamagoya2023)\n"
        )
    os.remove(output_file_path)
