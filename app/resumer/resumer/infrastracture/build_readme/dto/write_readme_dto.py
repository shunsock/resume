from typing import List

from pydantic import BaseModel, StrictStr


class WriteReadmeDto(BaseModel):
    output_file_path: StrictStr
    contents: List[str]
