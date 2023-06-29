from api_ex.domain.factory import UserFactory
from api_ex.domain.user import User
from api_ex.persistence.users_sql import UserPersistenceSql


class UserRepo:
    def __init__(self):
        self.__user_list = None
        self.__persistence = UserPersistenceSql("main_users.db")

    def get_all_users(self):
        self.refresh_cache()
        return self.__user_list

    def get_by_username(self, username: str):
        for u in [UserFactory.from_tuple(x) for x in self.__persistence.get_all_users()]:
            if u.username == username:
                return u

    def delete_user(self, username: str):
        self.__persistence.delete_user(username)
        self.refresh_cache()

    def add_user(self, user: User):
        self.__check_if_users_is_none()
        self.__persistence.add_user(user.username, user.email)
        self.__user_list.append(user)

    def update_user(self, username: str, new_username: str):
        self.__persistence.update_user(username, new_username)
        self.refresh_cache()

    def refresh_cache(self):
        self.__user_list = [UserFactory.from_tuple(x) for x in self.__persistence.get_all_users()]

    def __check_if_users_is_none(self):
        if self.__user_list is None:
            self.__user_list = [UserFactory.from_tuple(x) for x in self.__persistence.get_all_users()]

