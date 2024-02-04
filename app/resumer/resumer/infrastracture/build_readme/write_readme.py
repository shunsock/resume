from resumer.infrastracture.build_readme.dto.write_readme_dto import WriteReadmeDto


def write_readme(dto: WriteReadmeDto) -> None:
    with open(dto.output_file_path, "w") as file:
        for line in dto.contents:
            file.write(line + "\n")
