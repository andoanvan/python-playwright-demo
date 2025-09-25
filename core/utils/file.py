from pathlib import Path


class FileUtils:

    @staticmethod
    def get_root_path() -> str:
        return Path(__file__).resolve().parents[2].as_posix()

    @staticmethod
    def get_file_path(relative_path: str) -> str:
        return (Path(__file__).resolve().parents[2] / relative_path).as_posix()
