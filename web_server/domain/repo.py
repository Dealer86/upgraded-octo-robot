from web_server.domain.user import User


class UserRepository:
    def __init__(self):
        self.__users = []

    def add(self, user: User):
        self.__users.append(user)

    def get_all(self) -> list[User]:
        return self.__users

    def delete(self, name: str):
        self.__users = [u for u in self.__users if u.name != name]
        return self.__users
    
