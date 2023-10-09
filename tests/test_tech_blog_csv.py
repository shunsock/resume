import pytest
from pydantic import ValidationError

from src.models.tech_blog_csv import TechBlogCSV


def test_normal_test_case() -> None:
    try:
        test_case = TechBlogCSV(
            file_path="src/techblog/test_csv_file.csv",
            site_name="PR TIMES",
            tag_name="MLOps",
        )
        assert test_case.file_path == "src/techblog/test_csv_file.csv"
        assert test_case.site_name == "PR TIMES"
        assert test_case.tag_name == "MLOps"
    except ValidationError:
        assert False


def test_argument_field_error_case() -> None:
    with pytest.raises(ValidationError):
        TechBlogCSV(
            file_path="src/techblog/test_csv_file.csv",
            site_name="PR TIMES",
            tag_name="MLOps",
            test="test",
        )


def test_argument_type_error_case() -> None:
    with pytest.raises(ValidationError):
        TechBlogCSV(
            file_path="src/techblog/test_csv_file.csv",
            site_name="PR TIMES",
            tag_name=1,
        )


def test_file_path_is_not_found() -> None:
    with pytest.raises(ValidationError):
        TechBlogCSV(
            file_path="src/techblog/test_csv_file_not_found.csv",
            site_name="PR TIMES",
            tag_name="MLOps",
        )
