from core.utils.json import JsonUtils
from services.api.models.response.standard_ip_lookup.hostname_response_model import (
    HostnameResponse,
)
from services.api.models.response.standard_ip_lookup.ip_response_model import IPResponse


class IpStackJsonClient:
    ...

    def get_hostname_info_model_api(self, ip: str) -> HostnameResponse:
        """Fetch hostname information and convert to HostnameResponse model."""
        host_names = JsonUtils.read_json_file_as_list_model(
            file_path="data/test_data/ip_stack/hostname.json",
            model_class=HostnameResponse,
        )
        for host in host_names:
            if host.ip == ip:
                return host
        return host_names[0]

    def get_ip_info_model_api(self, ip: str) -> IPResponse:
        """Fetch IP information and convert to IPResponse model."""
        ip_infos = JsonUtils.read_json_file_as_list_model(
            file_path="data/test_data/ip_stack/lookup.json",
            model_class=IPResponse,
        )
        for info in ip_infos:
            if info.ip == ip:
                return info
        return ip_infos[0]
