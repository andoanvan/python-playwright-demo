"""Configuration management module."""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Configs:
    """Environment configuration class."""

    # URLs
    BASE_URL: str

    # Authentication
    AUTH_USERNAME: str
    AUTH_PASSWORD: str

    # Ip Stack
    IP_STACK_BASE_URL: str
    IP_STACK_ACCESS_KEY: str

    # Browser Configuration
    HEADLESS: bool
    RECORD_VIDEO: bool

    # API Configuration
    API_TIMEOUT: int
    API_RETRY_COUNT: int
    API_DEBUG: bool

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    _instance: Optional["Configs"] = None

    def __init__(self):
        """Initialize configuration from environment variables."""
        env = os.getenv("ACTIVE_ENV", "dev")
        env_file = f"configs/.env.{env}"

        if not os.path.exists(env_file):
            raise FileNotFoundError(f"Env file not found: {env_file}")

        # Load environment variables from file
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

        # URLs
        self.BASE_URL = os.getenv("BASE_URL", "")

        # Ip Stack
        self.IP_STACK_BASE_URL = os.getenv("IP_STACK_BASE_URL", "")
        self.IP_STACK_ACCESS_KEY = os.getenv("IP_STACK_ACCESS_KEY", "")

        # Authentication
        self.AUTH_USERNAME = os.getenv("AUTH_USERNAME", "")
        self.AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", "")

        # Browser Configuration
        self.HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
        self.RECORD_VIDEO = os.getenv("RECORD_VIDEO", "false").lower() == "true"

        # API Configuration
        self.API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))
        self.API_RETRY_COUNT = int(os.getenv("API_RETRY_COUNT", "3"))
        self.API_DEBUG = os.getenv("API_DEBUG", "false").lower() == "true"
        # Database Configuration
        self.DB_HOST = os.getenv("DB_HOST", "localhost")
        self.DB_PORT = int(os.getenv("DB_PORT", ""))
        self.DB_USER = os.getenv("DB_USER", "")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD", "")
        self.DB_NAME = os.getenv("DB_NAME", "")

    def __new__(cls):
        """Get singleton instance of Configs."""
        if not cls._instance:
            cls._instance = super(Configs, cls).__new__(cls)
        return cls._instance
