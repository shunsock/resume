from pathlib import Path
from typing import Annotated

from pydantic import BaseModel, StrictStr


class ReadBlogArticleFromCsvDto(BaseModel):
    """Data transfer object for reading blog articles from a CSV file."""

    blog_service_name: StrictStr
    file_path: Annotated[StrictStr, Path(exists=True)]
