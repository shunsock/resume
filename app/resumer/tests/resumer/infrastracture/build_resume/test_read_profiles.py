from resumer.infrastracture.build_readme.dto.read_profiles_dto import ReadProfilesDto
from resumer.infrastracture.build_readme.read_profiles import read_profiles


def test_read_profiles() -> None:
    dto = ReadProfilesDto(
        file_paths=[
            "resumer/data/test/infrastracture/build_resume/2_career.txt",
            "resumer/data/test/infrastracture/build_resume/5_presentation.txt",
        ]
    )
    expected_result = [
        "aiueo",
        "kakikukeko",
        "sasisuseso",
        "tatituteto",
        "naninuneno",
    ]
    result = read_profiles(dto=dto)

    assert result == expected_result
