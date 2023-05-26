import json
import os

from users_assets.asset import Asset
from users_assets.user import User


class UserFile:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def add_user(self, user: User):
        user_list = self.get_all()
        user_list.append(user)
        self.__save_all(user_list)

    def add_asset(self, user_name: str, asset: Asset):
        user_list = self.get_all()
        for user in user_list:
            if user.name == user_name:
                user.asset_list.append(asset)
                break
        self.__save_all(user_list)

    def get_all(self) -> list[User]:
        if not os.path.exists(self.__file_path):
            return []
        try:
            with open(self.__file_path) as f:
                content = f.read()
                decoded_content = json.loads(content)
                users_list = [User.from_dict(x) for x in decoded_content]
                return users_list
        except Exception as e:
            print(str(e))
            raise e

    def __save_all(self, user_list: list[User]):
        with open(self.__file_path, "w") as f:
            json.dump([user.to_dict() for user in user_list], f, indent=4)


if __name__ == "__main__":
    user1 = User("adis", "example@gmail.com")
    asset1 = Asset("goog", "USA")
    asset2 = Asset("appl", "USA")
    repo = UserFile("user_assets.json")
    repo.add_user(user1)
    repo.add_asset("adis", asset1)
    repo.add_asset("adis", asset2)

