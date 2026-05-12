import psycopg2

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