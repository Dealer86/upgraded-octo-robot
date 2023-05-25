from API_which_can_save_users.domain.user import User
from API_which_can_save_users.domain.user_factory import UserFactory
from API_which_can_save_users.persistence.users_sqlite import UsersSqlLite


class UserRepository:
    def __init__(self):
        self.__users_db = UsersSqlLite("persistence/users.db")
        self.__load_from_db()

    def add(self, user: User):
        self.__users_db.add(user.name, user.email)
        self.__load_from_db()

    def get_all(self) -> list[User]:
        return self.__users

    def delete(self, id_: int):
        self.__users_db.delete(id_)
        self.__users = [u for u in self.__users if u.id != id_]

    def __load_from_db(self):
        self.__users = [UserFactory.create_from_db(u) for u in self.__users_db.get_all()]

