import psycopg2 as db

class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database="test_bot_api",
            user="postgres",
            password="akrom_1102",
            host='localhost'
        )

        cursor = database.cursor()
        cursor.execute(query)

        data = ["insert", "create"]
        if query_type in data:
            database.commit()
            if query_type == "insert":
                return 'insert boldi'
            elif query_type == "create":
                return 'create boldi'

        else:
            return cursor.fetchall()