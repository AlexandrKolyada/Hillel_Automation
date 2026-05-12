import os
import pytest
import allure
from app.db_manager import DBManager
from app.users_table import UsersTable

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "mysecretpassword")


@pytest.fixture(scope="module")
def users_page():
    db = DBManager(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    db.connect()

    table = UsersTable(db)
    table.create_table_if_not_exists()

    yield table

    db.close()

@allure.feature("Test DB: Users table (CRUD)")
class TestUsersDatabase:

    def test_db_connection(self, users_page):
        with allure.step("Check connect to DB"):
            assert users_page.db.connection is not None
            assert users_page.db.connection.closed == 0

    def test_insert_and_select(self, users_page):
        user_id = users_page.insert_user("Alexandr PageObject", "alex_po@test.com")

        with allure.step("Verify that the ID of the created user is returned"):
            assert user_id is not None

        user = users_page.get_user_by_id(user_id)

        with allure.step("Validation of stored user data"):
            assert user is not None
            assert user['name'] == "Alexandr PageObject"
            assert user['email'] == "alex_po@test.com"

    def test_update(self, users_page):
        user_id = users_page.insert_user("Tester Allure", "allure@test.com")
        users_page.update_user_email(user_id, "new_allure@test.com")

        updated_user = users_page.get_user_by_id(user_id)

        with allure.step("Verify that the user's email was successfully updated in the DB"):
            assert updated_user['email'] == "new_allure@test.com"

    def test_delete(self, users_page):
        user_id = users_page.insert_user("To Delete PO", "delete_po@test.com")
        users_page.delete_user(user_id)

        deleted_user = users_page.get_user_by_id(user_id)

        with allure.step("Checking that a record no longer exists in the DB"):
            assert deleted_user is None