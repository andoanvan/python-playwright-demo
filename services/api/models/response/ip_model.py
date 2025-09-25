class IpModel:  # noqa: E501
    """Data model for IP information."""

    def __init__(self, data: dict):
        self.ip = data.get("ip")
        self.type = data.get("type")
        self.continent_code = data.get("continent_code")
        self.continent_name = data.get("continent_name")
        self.country_code = data.get("country_code")
        self.country_name = data.get("country_name")
        self.region_code = data.get("region_code")
        self.region_name = data.get("region_name")
        self.city = data.get("city")
        self.zip = data.get("zip")
        self.latitude = data.get("latitude")
        self.longitude = data.get("longitude")
        self.location = data.get("location", {})
        self.timezone = self.location.get("time_zone", {}) if self.location else {}
        self.currency = self.location.get("currency", {}) if self.location else {}
        self.connection = data.get("connection", {})
        self.security = data.get("security", {})
