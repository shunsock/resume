import os

from resumer.infrastracture.build_readme.dto.write_readme_dto import WriteReadmeDto
from resumer.infrastracture.build_readme.write_readme import write_readme


def test_write_readme() -> None:
    output_file_path = "resumer/data/test/infrastracture/build_resume/README.md"
    dto = WriteReadmeDto(
        output_file_path=output_file_path,
        contents=["contents"],
    )

    write_readme(dto)
    os.remove(output_file_path)
