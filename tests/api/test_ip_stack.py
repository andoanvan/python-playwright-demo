"""Tests for IP Stack API."""

import pytest

from services.controllers.ip_stack_controllers import IPStackController


class TestIPStack:
    """Test cases for IP Stack API."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Fixture providing IP Stack client."""
        self.ip_stack = IPStackController()

    @pytest.mark.debug
    def test_ip_lookup(self):
        """Test IP lookup with specific IP."""
        ip_response = self.ip_stack.get_ip_info_model_api("134.201.250.155")
        ip_data = self.ip_stack.get_ip_info_json("134.201.250.155")

        self.ip_stack.verify_ip_info_is_same(ip_response, ip_data)

    def test_hostname_lookup(self):
        """Test IP lookup with hostname."""
        hostname_response = self.ip_stack.get_hostname_info_model_api("8.8.8.8")
        hostname_data = self.ip_stack.get_hostname_info_json("8.8.8.8")

        self.ip_stack.verify_hostname_info_is_same(hostname_response, hostname_data)
