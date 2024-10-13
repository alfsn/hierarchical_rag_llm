import psycopg2
from psycopg2.extras import execute_values
from pgvector.psycopg2 import register_vector

class Database:
    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)
        register_vector(self.conn)

    def __del__(self):
        self.conn.close()

class FAQDatabase(Database):
    def get_all_faqs(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT question, embedding, category FROM faqs")
            return cur.fetchall()

    def add_faq(self, question, embedding, category):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO faqs (question, embedding, category) VALUES (%s, %s, %s)",
                (question, embedding, category)
            )
        self.conn.commit()

class ExternalInfoDatabase(Database):
    def get_relevant_info(self, embedding, limit=5):
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT content FROM external_info ORDER BY embedding <-> %s LIMIT %s",
                (embedding, limit)
            )
            return cur.fetchall()

class QADatabase(Database):
    def store(self, question, answer):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO qa_pairs (question, answer) VALUES (%s, %s)",
                (question, answer)
            )
        self.conn.commit()