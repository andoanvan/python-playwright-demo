from pydantic import BaseModel


class Language(BaseModel):
    """Language information from IP Stack response."""

    code: str
    name: str
    native: str
