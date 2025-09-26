import pytest
import allure
from services.controllers.user_db_controllers import UserController
from services.db.mock_data.clients.user_db_client import UserDBClient


class TestUserDb:
    """Test cases for User Database."""

    @pytest.fixture(autouse=True)
    def setup(self, db_client):
        self.user_controller = UserController(db_client)

    @pytest.mark.skip(reason="Skipping test")
    def test_users_data(self):
        users = self.user_controller.get_all_user_entities()
        allure.attach(name="Users", body=str(users))
        allure.step("Verify users data")
        assert len(users) >= 2
        allure.attach(name="User 0", body=str(users[0]))
        allure.attach(name="User 1", body=str(users[1]))
        assert users[0].name == "Alice"
        assert users[1].name == "Bob"
