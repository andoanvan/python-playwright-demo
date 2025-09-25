import json
from pathlib import Path
from typing import Any, TypeVar

from pydantic import BaseModel

from core.utils.file import FileUtils

T = TypeVar("T", bound=BaseModel)
from typing import Type


class JsonUtils:
    @staticmethod
    def read_json_file(file_path: str) -> Any:
        """Read and return JSON data from a file."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"JSON file not found: {file_path}")

        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def write_json_file(file_path: str, data: Any) -> None:
        """Write data to a JSON file."""
        path = Path(file_path)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def read_json_file_as_model(file_path: str, model_class: Type[T]) -> T:
        path = FileUtils.get_file_path(file_path)
        data = JsonUtils.read_json_file(path)
        return JsonUtils.read_json_as_model(data, model_class)

    @staticmethod
    def read_json_file_as_list_model(file_path: str, model_class: Type[T]) -> list[T]:
        path = FileUtils.get_file_path(file_path)
        data = JsonUtils.read_json_file(path)
        return JsonUtils.read_json_as_list_model(data, model_class)

    @staticmethod
    def read_json_as_model(json_str: Any, model_class: Type[T]) -> T:
        return model_class(**json_str)

    @staticmethod
    def read_json_as_list_model(json_str: Any, model_class: Type[T]) -> list[T]:
        return [model_class(**item) for item in json_str]
