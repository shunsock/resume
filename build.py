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
    # write header to README.md
    with open("README.md", "a") as f:
        f.write("## Tech Blog\n")
        f.write("| Site Name | Tag      | Title       |\n")
        f.write("| ------    |------    | -----------|\n")

    # write articles to README.md
    translate_csv_to_md_table.run(
        file_path="src/techblog/data/prtimes.csv",
        site_name="PR TIMES",
        tag_name="MLOps",
    )
    translate_csv_to_md_table.run(
        file_path="src/techblog/data/zenn.csv", site_name="Zenn", tag_name="Web/Stats"
    )
    translate_csv_to_md_table.run(
        file_path="src/techblog/data/toukei_no_mori.csv",
        site_name="Hello Statisicians!",
        tag_name="Machine Learning",
    )
    translate_csv_to_md_table.run(
        file_path="src/techblog/data/hatena.csv",
        site_name="Hatena Blog",
        tag_name="Conference",
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
