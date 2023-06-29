import sqlite3


class UserPersistenceSql:
    def __init__(self, filepath: str):
        self.__filepath = filepath

    def get_all_users(self) -> list[tuple]:
        with sqlite3.connect(self.__filepath) as db:
            cursor = db.cursor()
            try:
                cursor.execute("SELECT * FROM users")
                result = cursor.fetchall()
                return result
            except sqlite3.OperationalError as e:
                if "no such table" in str(e):
                    cursor.execute("CREATE TABLE users(username TEXT, email TEXT)")
                    db.commit()
                    return []

    def add_user(self, username: str, email: str):

        with sqlite3.connect(self.__filepath) as db:
            cursor = db.cursor()
            try:
                cursor.execute(f"INSERT INTO users(username, email) VALUES('{username}', '{email}')")
                db.commit()
            except sqlite3.OperationalError as e:
                if "no such table" in str(e):
                    cursor.execute("CREATE TABLE users(username TEXT, email TEXT)")

                cursor.execute(f"INSERT INTO users(username, email) VALUES('{username}', '{email}')")
            db.commit()

    def update_user(self, username: str, new_username: str):
        with sqlite3.connect(self.__filepath) as db:
            cursor = db.cursor()
            try:
                cursor.execute(f"UPDATE users SET username='{new_username}' WHERE username='{username}'")
                db.commit()
            except Exception as e:
                raise e

    def delete_user(self, username: str):
        with sqlite3.connect(self.__filepath) as db:
            cursor = db.cursor()
            try:
                cursor.execute(f"DELETE FROM users WHERE username='{username}'")
                db.commit()
            except Exception as e:
                raise e








