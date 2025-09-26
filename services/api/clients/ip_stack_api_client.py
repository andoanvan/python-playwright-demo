"""Client for interacting with the IP Stack API."""

from requests import Response

from configs.configs import Configs
from core.api.base_request import BaseRequest
from services.api.endpoints.standard_ip_lookup_endpoint import ip_endpoints


class IpStackClient(BaseRequest):
    """Client for interacting with the IP Stack API."""

    def __init__(self):
        super().__init__(base_url=Configs().IP_STACK_BASE_URL)
        self._access_key = Configs().IP_STACK_ACCESS_KEY

    def get_basic_standard_ip_lookup(self, ip_address: str) -> Response:
        """Get basic standard IP lookup information.

        Args:
            ip_address (str): The IP address to look up.

        Returns:
            IPResponse: Parsed API response.
        """
        return self.get(
            endpoint=ip_endpoints.LOOKUP.format(ip_address=ip_address),
            params={"access_key": self._access_key},
        )

    def get_hostname(self, ip_address: str) -> Response:
        """Get hostname information for the given IP address.

        Args:
            ip_address (str): The IP address to look up.

        Returns:
            IPResponse: Parsed API response including hostname.
        """
        return self.get(
            endpoint=ip_endpoints.HOSTNAME.format(ip_address=ip_address),
            params={"access_key": self._access_key},
        )
