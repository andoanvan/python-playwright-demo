import psycopg2
from typing import List, Dict


class PostgresClient:
    def __init__(self, host, port, user, password, db):
        self.conn = psycopg2.connect(
            host=host, port=port, user=user, password=password, dbname=db
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query: str):
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
