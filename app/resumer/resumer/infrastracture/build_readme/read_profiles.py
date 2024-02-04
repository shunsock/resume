from typing import List

from resumer.infrastracture.build_readme.dto.read_profiles_dto import ReadProfilesDto
from resumer.infrastracture.helper.text_file_to_list import text_file_to_list


def read_profiles(dto: ReadProfilesDto) -> List[str]:
    # we can not use name `file`
    # because it is a built-in function
    profile_section_lines: List[str] = []

    for file_ in dto.file_paths:
        lines: List[str] = text_file_to_list(file_)
        for line in lines:
            profile_section_lines.append(line.replace("\n", ""))

    return profile_section_lines
