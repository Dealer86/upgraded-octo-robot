import json
import os

from add_asset_to_user_write_in_json_list_or_dict.class_asset import Asset
from add_asset_to_user_write_in_json_list_or_dict.class_user import User


class UserFile:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all(self) -> list[User]:
        if not os.path.exists(self.__file_path):
            return []
        with open(self.__file_path) as f:
            content = f.read()
        data = json.loads(content)
        return [User.from_tuple(u) for u in data]

    def add(self, user: User):
        user_list = self.get_all()
        user_list.append(user)
        self.__save_to_file(user_list)

    def add_asset(self, user: User, asset: Asset):
        user_list = self.get_all()
        for u in user_list:
            if u.id_ == user.id_:
                u.asset.append(asset)
        self.__save_to_file(user_list)

    def __save_to_file(self, list_user: list[User]):
        data = [u.to_tuple() for u in list_user]
        prep_data = json.dumps(data, indent=4)
        with open(self.__file_path, "w") as f:
            f.write(prep_data)


if __name__ == "__main__":
    user1 = User(1, "random")
    user2 = User(2, "not random")
    repo = UserFile("lista.json")

    asset1 = Asset("Apple", 101, "Romania")

    repo.add_asset(user2, asset1)
