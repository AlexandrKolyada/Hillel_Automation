import os
import pytest
from app.db_manager import DBManager

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "testdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "secret_pass")


@pytest.fixture(scope="module")
def db():

    manager = DBManager(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    manager.connect()
    manager.create_table()
    yield manager
    manager.close()


def test_db_connection(db):
    assert db.connection is not None
    assert db.connection.closed == 0


def test_insert_and_select(db):
    user_id = db.insert_user("Alexandr", "alex@test.com")
    assert user_id is not None

    user = db.get_user_by_id(user_id)
    assert user is not None
    assert user['name'] == "Alexandr"
    assert user['email'] == "alex@test.com"


def test_update(db):
    user_id = db.insert_user("Tester", "test@test.com")
    db.update_user_email(user_id, "new_test@test.com")

    updated_user = db.get_user_by_id(user_id)
    assert updated_user['email'] == "new_test@test.com"


def test_delete(db):
    user_id = db.insert_user("To Delete", "delete@test.com")
    db.delete_user(user_id)

    deleted_user = db.get_user_by_id(user_id)
    assert deleted_user is None