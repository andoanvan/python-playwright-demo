"""Pytest configuration and fixtures."""

import pytest
from core.db.postgres_client import PostgresClient

from configs.configs import Configs


@pytest.fixture(scope="session")
def db_client():
    """Fixture to provide a database client."""

    db = PostgresClient(
        host=Configs().DB_HOST,
        port=Configs().DB_PORT,
        user=Configs().DB_USER,
        password=Configs().DB_PASSWORD,
        db=Configs().DB_NAME,
    )  # Ensure to close the connection after tests are done

    yield db
    db.close()
