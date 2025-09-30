from typing import List
from core.db.postgres_client import PostgresClient
from services.db.entites.user_entity import UserEntity


class UserDBClient:
    def __init__(self, db_client: PostgresClient):
        self.db_client = db_client

    def get_all_users(self) -> List[tuple]:
        return self.db_client.execute_query("SELECT id, name, email FROM users")

    def get_user_by_id(self, id: int) -> tuple:
        return self.db_client.execute_query(
            f"SELECT id, name, email FROM users WHERE id = {id}"
        )

    def create_user(self, user: UserEntity) -> None:
        self.db_client.execute_query(
            f"INSERT INTO users (id, name, email) VALUES ({user.id}, {user.name}, {user.email})"
        )

    def update_user(self, user: UserEntity) -> None:
        self.db_client.execute_query(
            f"UPDATE users SET name = {user.name}, email = {user.email} WHERE id = {user.id}"
        )

    def delete_user(self, id: int) -> None:
        self.db_client.execute_query(f"DELETE FROM users WHERE id = {id}")
