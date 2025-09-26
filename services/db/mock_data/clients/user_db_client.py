from typing import List
from core.db.postgres_client import PostgresClient


class UserDBClient:
    def __init__(self, db_client: PostgresClient):
        self.db_client = db_client

    def get_all_users(self) -> List[tuple]:
        return self.db_client.execute_query("SELECT id, name, email FROM users")
