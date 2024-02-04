from typing import List

from pydantic import BaseModel


class ReadProfilesDto(BaseModel):
    file_paths: List[str]
