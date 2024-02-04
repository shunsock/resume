from resumer.domain.readme.readme import Readme
from resumer.infrastracture.build_readme.dto.read_profiles_dto import ReadProfilesDto
from resumer.infrastracture.build_readme.dto.write_readme_dto import WriteReadmeDto
from resumer.infrastracture.build_readme.read_profiles import read_profiles
from resumer.infrastracture.build_readme.write_readme import write_readme


def update_readme() -> None:
    readme: Readme = Readme()

    # get List[str] from readme with os module
    # and pass it to read_profiles
    file_paths = readme.get_profile_paths_under_profile_directory()

    profiles = read_profiles(
        ReadProfilesDto(
            file_paths=file_paths,
        )
    )
    write_readme(
        WriteReadmeDto(
            output_file_path=str(readme.output_file_path),
            contents=profiles,
        )
    )
