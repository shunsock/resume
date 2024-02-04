from pathlib import Path
from typing import List

from pydantic import BaseModel, FilePath


class Readme(BaseModel):
    output_file_path: FilePath = FilePath("resumer/data/readme/README.md")
    profile_file_path: FilePath = FilePath("resumer/data/profile")
    blog_articles_file_path: FilePath = FilePath("resumer/data/blog_article")

    def get_profile_paths_under_profile_directory(self) -> List[str]:
        # Convert the FilePath to a Path object to use pathlib methods
        profile_path = Path(str(self.profile_file_path))

        # List to hold the paths
        file_paths = []

        # Use rglob to find all files under the directory
        for file_path in profile_path.rglob("*"):
            # Check if it's a file (and not a directory)
            if file_path.is_file():
                # Append the string representation of the path to the list
                file_paths.append(str(file_path))

        return file_paths
