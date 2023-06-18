import os
import json

from solid.single_responsibility_principle import Logger
from to_list_to_dict.user import User
log = Logger("2.log")


class UserDictRepo:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all(self):
        log.logger("UserDictRepo get all method is called", level="info")
        if not os.path.exists(self.__file_path):
            return []
        try:
            with open(self.__file_path) as f:
                content = f.read()
            content = json.loads(content)
            print(content)
            return [User.from_dict(x) for x in content]
        except Exception as e:
            log.logger(f"Method get_all can not be used. Exception: {str(e)}", level="error")
            print(str(e))
            return []

    def add(self, user: User):
        user_list = self.get_all()
        user_list.append(user)

        json_dict = [User.to_dict(x) for x in user_list]
        json_dict = json.dumps(json_dict, indent=4)
        try:
            with open(self.__file_path, "w") as f:
                f.write(json_dict)
        except Exception as e:
            raise e

    def update(self, user: User, new_username: str):
        user_list = self.get_all()
        for u in user_list:
            if u.user_id == user.user_id:
                u.username = new_username
        json_data = [User.to_dict(x) for x in user_list]
        json_data = json.dumps(json_data, indent=4)
        with open(self.__file_path, "w") as f:
            f.write(json_data)

    def delete(self, user: User):
        user_list = self.get_all()
        for u in user_list:
            if u.user_id == user.user_id:
                user_list.remove(u)
        json_data = [User.to_dict(x) for x in user_list]
        json_data = json.dumps(json_data)
        with open(self.__file_path, "w") as f:
            f.write(json_data)


user1 = User(1, "primul")

repo = UserDictRepo("user_dict.json")

# repo.add(user1)
# repo.update(user1, "alt nume nou")
# repo.delete(user1)
