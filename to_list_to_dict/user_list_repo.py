import os

from to_list_to_dict.user import User
import json


class UserListRepo:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def write_to_file(self, user: User):
        user_list = self.get_all()
        if user.user_id in [x.user_id for x in user_list]:
            raise Exception("Userul este in lista")
        user_list.append(user)
        user_list = [User.to_list(x) for x in user_list]
        json_user_list = json.dumps(user_list, indent=4)
        try:
            with open(self.__file_path, "w") as f:
                f.write(json_user_list)
        except Exception as e:
            raise e

    def get_all(self) -> list[User]:
        if not os.path.exists(self.__file_path):
            return []
        try:
            with open(self.__file_path) as f:
                content = f.read()
            objects_list = json.loads(content)
            return [User.from_list(x) for x in objects_list]
        except Exception as e:
            print(str(e) + "error!!!")
            return []

    def update(self, user: User, username: str):
        user_list = self.get_all()

        for every_user in user_list:
            if every_user.user_id == user.user_id:
                every_user.username = username
            else:
                raise Exception("No user found with that id")
        user_list = [User.to_list(x) for x in user_list]
        json_list = json.dumps(user_list, indent=4)
        with open(self.__file_path, "w") as f:
            f.write(json_list)

    def delete(self, user: User):
        user_list = self.get_all()
        for u in user_list:
            if u.user_id == user.user_id:
                user_list.remove(u)
        user_list = [User.to_list(x) for x in user_list]
        json_object = json.dumps(user_list, indent=4)
        with open(self.__file_path, "w") as f:
            f.write(json_object)
