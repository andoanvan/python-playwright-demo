from typing import Optional

from pydantic import BaseModel

from services.api.models.response.standard_ip_lookup.location_response_model import (
    Location,
)


class HostnameResponse(BaseModel):
    hostname: str
    ip: str
    type: str
    continent_code: str
    continent_name: str
    country_code: str
    country_name: str
    region_code: str
    region_name: str
    city: str
    zip: str
    latitude: float
    longitude: float
    msa: Optional[str] = None
    dma: Optional[str] = None
    radius: Optional[int] = None
    ip_routing_type: Optional[str] = None
    connection_type: Optional[str] = None
    location: Optional[Location] = None
