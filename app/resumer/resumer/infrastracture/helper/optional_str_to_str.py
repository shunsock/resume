from typing import Optional


def optional_str_to_str(text: Optional[str]) -> str:
    """Converts an Optional[str] to a str."""
    if text is None:
        return ""
    return text
