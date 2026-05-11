import psycopg2
from psycopg2.extras import DictCursor

class DBManager:
    def __init__(self, host, database, user, password, port=5432):
        self.conn_params = {
            "host": host,
            "database": database,
            "user": user,
            "password": password,
            "port": port
        }
        self.connection = None

    def connect(self):
        if not self.connection or self.connection.closed:
            self.connection = psycopg2.connect(**self.conn_params)
        return self.connection

    def close(self):
        if self.connection and not self.connection.closed:
            self.connection.close()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()

    def insert_user(self, name, email):
        query = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;"
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (name, email))
                user_id = cursor.fetchone()[0]
                conn.commit()
                return user_id

    def get_user_by_id(self, user_id):
        query = "SELECT id, name, email FROM users WHERE id = %s;"
        with self.connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (user_id,))
                return cursor.fetchone()

    def update_user_email(self, user_id, new_email):
        query = "UPDATE users SET email = %s WHERE id = %s;"
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (new_email, user_id))
                conn.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s;"
        with self.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (user_id,))
                conn.commit()