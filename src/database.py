import sqlite3


connection = sqlite3.connect("database.db")
cursor = connection.cursor()


class DataBase:

    @staticmethod
    def create_table() -> None:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
            telegram_id TEXT,
            first_name TEXT,
            last_name TEXT,
            balance INTEGER
        )""")

        connection.commit()

    @staticmethod
    def get_user(id: int):
        cursor.execute("SELECT * FROM Users WHERE telegram_id = ?", [id])

        return cursor.fetchone()        

    @staticmethod
    def add_user(id: int, first_name: str, last_name: str) -> None:
        cursor.execute("INSERT INTO Users(telegram_id, first_name, last_name, balance) VALUES (?, ?, ?, ?)", [id, first_name, last_name, 0])
        connection.commit()
