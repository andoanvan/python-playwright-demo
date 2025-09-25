import allure

from services.api.clients.ip_stack_api_client import IpStackClient
from services.api.models.response.standard_ip_lookup.hostname_response_model import (
    HostnameResponse,
)
from services.api.models.response.standard_ip_lookup.ip_response_model import IPResponse
from services.db.mock_data.clients.ip_stack_json_client import IpStackJsonClient


class IPStackController:
    def __init__(self):
        self.ip_client = IpStackClient()
        self.ip_json_client = IpStackJsonClient()

    def get_ip_info_api(self, ip_address):
        return self.ip_client.get_basic_standard_ip_lookup(ip_address)

    def get_hostname_info_api(self, hostname):
        return self.ip_client.get_hostname(hostname)

    @allure.step("Get IP information for '{ip_address}' and convert to model")
    def get_ip_info_model_api(self, ip_address):
        response = self.get_ip_info_api(ip_address)
        assert response.status_code == 200
        return self.ip_client.convert_response_to_model(response, IPResponse)

    @allure.step("Get hostname information for '{hostname}' and convert to model")
    def get_hostname_info_model_api(self, hostname):
        response = self.get_hostname_info_api(hostname)
        assert response.status_code == 200
        return self.ip_client.convert_response_to_model(response, HostnameResponse)

    @allure.step("Get IP information for '{ip_address}' from JSON client")
    def get_ip_info_json(self, ip_address):
        return self.ip_json_client.get_ip_info_model_api(ip_address)

    @allure.step("Get hostname information for '{hostname}' from JSON client")
    def get_hostname_info_json(self, hostname):
        return self.ip_json_client.get_hostname_info_model_api(hostname)

    @allure.step("Verify two IP information objects are the same")
    def verify_ip_info_is_same(self, ip_info_1, ip_info_2):
        self.compare_two_models(ip_info_1, ip_info_2)

    @allure.step("Verify two hostname information objects are the same")
    def verify_hostname_info_is_same(self, hostname_info_1, hostname_info_2):
        self.compare_two_models(hostname_info_1, hostname_info_2)

    def compare_two_models(self, model1, model2):
        """Compare two data models for equality."""
        assert model1 == model2
