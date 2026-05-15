import allure
import psycopg
from psycopg.rows import dict_row


class UsersTable:
    """Page Object для взаємодії з таблицею 'users' за допомогою psycopg3"""

    def __init__(self, db_manager):
        self.db = db_manager

    @allure.step("Створення таблиці 'users', якщо вона не існує")
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

    @allure.step("Вставка (Insert) нового користувача: ім'ям '{name}', email '{email}'")
    def insert_user(self, name, email):
        query = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;"
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (name, email))
                user_id = cursor.fetchone()[0]
                conn.commit()
                return user_id

    @allure.step("Вибірка (Select) користувача з ID: {user_id}")
    def get_user_by_id(self, user_id):
        query = "SELECT id, name, email FROM users WHERE id = %s;"
        with self.db.connect() as conn:
            # У psycopg3 для повернення словників використовується row_factory
            with conn.cursor(row_factory=dict_row) as cursor:
                cursor.execute(query, (user_id,))
                return cursor.fetchone()

    @allure.step("Оновлення (Update) пошти користувача з ID {user_id} на новий email: '{new_email}'")
    def update_user_email(self, user_id, new_email):
        query = "UPDATE users SET email = %s WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (new_email, user_id))
                conn.commit()

    @allure.step("Видалення (Delete) користувача з ID: {user_id}")
    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s;"
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (user_id,))
                conn.commit()