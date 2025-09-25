from pydantic import BaseModel


class Connection(BaseModel):
    """Connection information."""

    asn: int
    isp: str
