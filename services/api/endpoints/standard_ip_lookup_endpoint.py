"""API endpoints configuration."""

from dataclasses import dataclass

from configs.configs import Configs
from core.utils.json import JsonUtils


@dataclass
class IPEndpoints:
    """IP Stack API endpoints."""

    LOOKUP: str
    HOSTNAME: str

    @classmethod
    def init(cls) -> "IPEndpoints":
        """Initialize IP endpoints.

        Returns:
            IPEndpoints: Configured IP endpoints
        """
        ip_stack = JsonUtils.read_json_file("data/endpoints/ip_stack.json").get(
            "standard_ip_lookup", {}
        )
        return cls(
            LOOKUP=ip_stack.get("lookup"),
            HOSTNAME=ip_stack.get("hostname"),
        )


# Initialize singleton instances
ip_endpoints = IPEndpoints.init()
