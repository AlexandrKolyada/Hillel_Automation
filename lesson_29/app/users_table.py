import allure
from psycopg2.extras import DictCursor


class UsersTable:

    def __init__(self, db_manager):
        self.db = db_manager

    @allure.step("Create table 'users', if it exists")
    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()

    @allure.step("Insert new user: name '{name}', email '{email}'")
    def insert_user(self, name, email):
        query = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;"
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (name, email))
                user_id = cursor.fetchone()[0]
                conn.commit()
                return user_id

    @allure.step("Select user with ID: {user_id}")
    def get_user_by_id(self, user_id):
        query = "SELECT id, name, email FROM users WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (user_id,))
                return cursor.fetchone()

    @allure.step("Update user mail with ID {user_id} to new one email: '{new_email}'")
    def update_user_email(self, user_id, new_email):
        query = "UPDATE users SET email = %s WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (new_email, user_id))
                conn.commit()

    @allure.step("Delete) user with ID: {user_id}")
    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (user_id,))
                conn.commit()