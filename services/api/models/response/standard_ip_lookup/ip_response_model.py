"""IP Stack API response models."""

from typing import Optional

from pydantic import BaseModel

from services.api.models.response.standard_ip_lookup.connection_response_model import (
    Connection,
)
from services.api.models.response.standard_ip_lookup.currency_response_model import (
    Currency,
)
from services.api.models.response.standard_ip_lookup.location_response_model import (
    Location,
)
from services.api.models.response.standard_ip_lookup.timezone_response_model import (
    TimeZone,
)


class IPResponse(BaseModel):
    """Main response model for IP Stack API."""

    ip: str
    type: str
    country_code: str
    country_name: str
    region_code: str
    region_name: str
    city: str
    zip: str
    latitude: float
    longitude: float
    continent_name: Optional[str] = None
    continent_code: Optional[str] = None
    location: Optional[Location] = None
    time_zone: Optional[TimeZone] = None
    currency: Optional[Currency] = None
    connection: Optional[Connection] = None
