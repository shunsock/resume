from typing import List

from src.service import (supply_file_content, supply_path_list,
                         translate_csv_to_md_table)


def write_techblog_to_readme() -> None:
    """
    Writes techblog to README.md

    Parameters
    ======
    None

    Returns
    ======
    None
    """
    from src.models.tech_blog_csv import TECH_BLOG_CSV_LIST

    # write header to README.md
    with open("README.md", "a") as f:
        f.write("## Tech Blog\n")
        f.write("| Site Name | Tag      | Title       |\n")
        f.write("| ------    |------    | -----------|\n")

    for tech_blog in TECH_BLOG_CSV_LIST:
        translate_csv_to_md_table.run(
            file_path=tech_blog.file_path,
            site_name=tech_blog.site_name,
            tag_name=tech_blog.tag_name,
        )


def write_profile_to_readme() -> None:
    """
    Writes profile to README.md

    Parameters
    ======
    None

    Returns
    ======
    None
    """
    # write profile to README.md
    files_: List[str] = supply_path_list.get("src/profile/")
    files_ = sorted(files_)

    # we can not use name `file`
    # because it is a built-in function
    with open("README.md", "w") as readme:
        for file_ in files_:
            lines: List[str] = supply_file_content.get(file_)
            for line in lines:
                # print(line)
                readme.write(line)
            readme.write("\n")


if __name__ == "__main__":
    write_profile_to_readme()
    write_techblog_to_readme()
