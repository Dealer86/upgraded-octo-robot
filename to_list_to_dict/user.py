import json
import os


class User:
    def __init__(self, user_id: int, username: str):
        self.__user_id = user_id
        self.__username = username

    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        if len(new_username) < 5:
            raise Exception("Username trebuie sa aiba mai mult de 5 charactere")
        self.__username = new_username

    def to_dict(self) -> dict:
        return {"user_id": self.user_id, "username": self.username}

    @classmethod
    def from_dict(cls, di: dict):
        return User(user_id=di["user_id"], username=di["username"])

    def to_list(self) -> tuple:
        return self.user_id, self.username

    @classmethod
    def from_list(cls, info: tuple):
        return User(user_id=info[0], username=info[1])
