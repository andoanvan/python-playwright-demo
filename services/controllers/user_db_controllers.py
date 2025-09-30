from typing import List
import allure
from core.db.postgres_client import PostgresClient
from services.db.entites.user_entity import UserEntity
from services.db.mock_data.clients.user_db_client import UserDBClient


class UserController:
    def __init__(self, db_client: PostgresClient):
        self.db_client = db_client

    @allure.step("Get all user entities")
    def get_all_user_entities(self) -> List[UserEntity]:
        result = UserDBClient(self.db_client).get_all_users()
        return [UserEntity(*r) for r in result]  # Alternative unpacking method

    @allure.step("Get user entity by id")
    def get_user_entity_by_id(self, id: int) -> UserEntity:
        result = UserDBClient(self.db_client).get_user_by_id(id)
        return UserEntity(*result)
