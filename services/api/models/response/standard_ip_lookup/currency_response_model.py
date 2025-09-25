from pydantic import BaseModel


class Currency(BaseModel):
    """Currency information."""

    code: str
    name: str
    plural: str
    symbol: str
    symbol_native: str
