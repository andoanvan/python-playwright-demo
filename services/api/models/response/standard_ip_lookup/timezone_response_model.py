from pydantic import BaseModel


class TimeZone(BaseModel):
    """Time zone information from IP Stack response."""

    id: str
    current_time: str
    gmt_offset: int
    code: str
    is_daylight_saving: bool
