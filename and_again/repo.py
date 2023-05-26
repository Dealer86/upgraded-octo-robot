import json
import os

from and_again.asset import Asset
from and_again.uzar import User


class UserFile:
    def __init__(self, file_path):
        self.__file_path = file_path

    def get_all(self) -> list[User]:
        if not os.path.exists(self.__file_path):
            return []
        try:
            with open(self.__file_path) as f:
                json_content = f.read()
                content_objects = json.loads(json_content)
                return [User.from_dict(u) for u in content_objects]
        except Exception as e:
            print(str(e))
            raise e

    def add_asset_to_user(self, user: User, asset: Asset):
        user_list = self.get_all()
        for u in user_list:
            if u.id_ == user.id_ and (asset.ticker not in [a.ticker for a in u.asset]):
                print(asset.ticker)
                print([a.ticker for a in u.asset])
                u.asset.append(asset)
            else:
                print("Asset already in list")
        self.__save_to_file(user_list)

    def add(self, user: User):
        user_list = self.get_all()
        user_list.append(user)
        self.__save_to_file(user_list)

    def __save_to_file(self, user_list: list[User]):
        data = [user.to_dict() for user in user_list]
        json_prep = json.dumps(data, indent=4)
        with open(self.__file_path, "w") as f:
            f.write(json_prep)


if __name__ == "__main__":
    user1 = User(1, "adi")
    repo = UserFile("uzar.json")
    # repo.add(user1)
    asset1 = Asset("Mar", 100, "ROMANIA")
    repo.add_asset_to_user(user1, asset1)
