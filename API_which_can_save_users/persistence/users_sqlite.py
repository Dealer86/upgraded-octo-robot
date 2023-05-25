import sqlite3


class UsersSqlLite:
    def __init__(self, path: str = "users.db"):
        self.__path = path

    def get_all(self) -> list[tuple]:
        with sqlite3.connect(self.__path) as db:
            cursor = db.cursor()
            cmd = "SELECT * FROM users"
            try:
                cursor.execute(cmd)
            except sqlite3.OperationalError as e:
                if "no such table" in str(e):
                    return []
            else:
                return cursor.fetchall()

    def add(self, name: str, email: str):
        cmd = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
        try:
            self.__execute_cmd(cmd)
        except sqlite3.OperationalError as e:
            if "no such table" in str(e):
                self.create_table()
                self.__execute_cmd(cmd)

    def delete(self, id_: int):
        cmd = f"DELETE FROM users WHERE id={id_}"
        self.__execute_cmd(cmd)

    def create_table(self):
        cmd = "CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, " \
              "email TEXT NOT NULL, films TEXT, shows TEXT)"
        self.__execute_cmd(cmd)

    def __execute_cmd(self, cmd):
        with sqlite3.connect(self.__path) as db:
            cursor = db.cursor()
            cursor.execute(cmd)
            db.commit()



