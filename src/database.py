import sqlite3


class Database:
    def __init__(self, db_name="test_orchestrator.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)
    
    def create_tables(self):
        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_suites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT        
                       
        )

        """)

        conn.commit()

        conn.close()

        print("Tables Created Succesfully!")

    def add_test_suite(self, name, description):
        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO test_suites ( name, description)
            VALUES (?, ?)
            """,
            (name, description)
        )

        conn.commit()
        
        conn.close()

        print("Test Suite Added successfully!")
    

    def get_test_suites(self):
        conn = self.connect()


        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM test_suites
            """
        )

        suites = cursor.fetchall()

        conn.close()

        return suites