from pydantic import BaseModel

from services.api.models.response.standard_ip_lookup.languages_response_model import (
    Language,
)


class Location(BaseModel):
    """Location information from IP Stack response."""

    geoname_id: int
    capital: str
    country_flag: str
    country_flag_emoji: str
    country_flag_emoji_unicode: str
    calling_code: str
    is_eu: bool
    languages: list[Language]
