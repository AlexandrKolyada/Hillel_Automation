import psycopg


class DBManager:

    def __init__(self, host, database, user, password, port=5432):
        self.conn_string = f"host={host} dbname={database} user={user} password={password} port={port}"
        self.connection = None

    def connect(self):
        if not self.connection or self.connection.closed:
            self.connection = psycopg.connect(self.conn_string)
        return self.connection

    def close(self):
        if self.connection and not self.connection.closed:
            self.connection.close()