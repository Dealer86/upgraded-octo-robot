from API_which_can_save_users.domain.user import User
from API_which_can_save_users.domain.user_factory import UserFactory
from API_which_can_save_users.persistence.users_sqlite import UsersSqlLite


class InvalidUserId(Exception):
    pass


class UserRepository:
    def __init__(self):
        self.__users_db = UsersSqlLite("persistence/users.db")
        self.__load_from_db()

    def add(self, user: User):
        self.__users_db.add(user.name, user.email)
        self.__load_from_db()


    def get_all(self) -> list[User]:
        print([u for u in self.__users if u.id == 2])
        return self.__users

    def delete(self, id_: int):
        self.__users_db.delete(id_)
        self.__users = [u for u in self.__users if u.id != id_]

    def get_by_id(self, id_: int) -> User:
        user_tuple = self.__users_db.get_by_id(id_)
        if user_tuple is None:
            raise InvalidUserId("User id does not exist")
        our_user = UserFactory.create_from_db(user_tuple)
        return our_user

    def update(self, user_id: int, username: str):
        self.__users_db.update(user_id, username)
        self.__load_from_db()


    def __load_from_db(self):
        self.__users = [UserFactory.create_from_db(u) for u in self.__users_db.get_all()]
