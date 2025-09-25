import logging
from typing import Any, Dict, Optional, TypeVar

import allure
from pydantic import BaseModel
from requests import Response, Session

from core.utils.json import JsonUtils

T = TypeVar("T", bound=BaseModel)
from typing import Type

logger = logging.getLogger(__name__)


class BaseRequest:
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        self.session = Session()
        if headers:
            self.session.headers.update(headers)

    def request(self, method: str, endpoint: str, **kwargs: Any) -> Response:
        """Send an HTTP request.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint: The endpoint path (will be joined with base_url)
            **kwargs: Additional arguments to pass to the request (params, data, json, headers, etc.)

        Returns:
            Response object
        """
        # Ensure clean URL joining by stripping slashes
        base = self.base_url.rstrip("/")
        path = endpoint.lstrip("/")
        url = f"{base}/{path}"
        allure.attach(name="Request URL", body=url)
        if "params" in kwargs:
            allure.attach(name="Request Params", body=str(kwargs["params"]))
        if "data" in kwargs:
            allure.attach(name="Request Data", body=str(kwargs["data"]))
        if "json" in kwargs:
            allure.attach(name="Request JSON", body=str(kwargs["json"]))
        response = self.session.request(method=method.upper(), url=url, **kwargs)
        response.raise_for_status()
        allure.attach(name="Response Status Code", body=str(response.status_code))
        allure.attach(name="Response Content", body=response.text)
        return response

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Response:
        """Send a GET request.

        Args:
            endpoint: The endpoint path (will be joined with base_url)
            params: Query parameters to include in the request
            **kwargs: Additional arguments to pass to the request (headers, etc.)

        Returns:
            Response object
        """
        return self.request("GET", endpoint, params=params, **kwargs)

    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Response:
        """Send a POST request.

        Args:
            endpoint: The endpoint path (will be joined with base_url)
            data: Form data to include in the request
            json: JSON data to include in the request
            **kwargs: Additional arguments to pass to the request (headers, etc.)

        Returns:
            Response object
        """
        return self.request("POST", endpoint, data=data, json=json, **kwargs)

    def put(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Response:
        """Send a PUT request.

        Args:
            endpoint: The endpoint path (will be joined with base_url)
            data: Form data to include in the request
            json: JSON data to include in the request
            **kwargs: Additional arguments to pass to the request (headers, etc.)

        Returns:
            Response object
        """
        return self.request("PUT", endpoint, data=data, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> Response:
        """Send a DELETE request.

        Args:
            endpoint: The endpoint path (will be joined with base_url)
            **kwargs: Additional arguments to pass to the request (headers, etc.)

        Returns:
            Response object
        """
        return self.request("DELETE", endpoint, **kwargs)

    def convert_response_to_model(self, response: Response, model_class: Type[T]) -> T:
        """Convert response JSON to a specified model.

        Args:
            response: The Response object from requests
            model: The model class to convert the JSON into

        Returns:
            An instance of the model populated with the response data
        """
        return JsonUtils.read_json_as_model(response.json(), model_class)
