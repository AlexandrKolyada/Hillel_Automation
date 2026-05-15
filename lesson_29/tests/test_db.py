import pytest
import allure
import time
from app.db_manager import DBManager
from app.users_table import UsersTable


@pytest.fixture(scope="class")
def db_manager():
    manager = DBManager(
        host="host.docker.internal",
        database="postgres",
        user="postgres",
        password="mysecretpassword"
    )
    manager.connect()
    yield manager
    manager.close()


@pytest.fixture(scope="class")
def users_page(db_manager):
    page = UsersTable(db_manager)
    page.create_table_if_not_exists()
    return page

class TestUsersDatabase:

    def test_db_connection(self, users_page):
        with allure.step("check connect DB"):
            assert users_page.db.connection is not None
            assert users_page.db.connection.closed is False

    def test_insert_and_select(self, users_page):
        unique_suffix = int(time.time())
        email = f"alex_po_{unique_suffix}@test.com"

        user_id = users_page.insert_user("Alexandr PageObject", email)

        with allure.step("Verifying the selection of the created user"):
            user = users_page.get_user_by_id(user_id)
            assert user is not None
            assert user['name'] == "Alexandr PageObject"
            assert user['email'] == email

    def test_update(self, users_page):
        unique_suffix = int(time.time())
        email_start = f"allure_{unique_suffix}@test.com"
        email_new = f"new_allure_{unique_suffix}@test.com"

        user_id = users_page.insert_user("Tester Allure", email_start)
        users_page.update_user_email(user_id, email_new)

        with allure.step("check email update"):
            user = users_page.get_user_by_id(user_id)
            assert user['email'] == email_new

    def test_delete(self, users_page):
        unique_suffix = int(time.time())
        email = f"delete_{unique_suffix}@test.com"

        user_id = users_page.insert_user("User For Delete", email)
        users_page.delete_user(user_id)

        with allure.step("check user deleting"):
            user = users_page.get_user_by_id(user_id)
            assert user is None