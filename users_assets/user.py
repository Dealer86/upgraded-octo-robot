from users_assets.asset import Asset


class User:
    def __init__(self, name: str, email: str, asset_list: list[Asset] = None):
        self.__name = name
        self.__email = email
        self.__asset_list = asset_list if asset_list else []

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def asset_list(self):
        return self.__asset_list

    def to_dict(self) -> dict:
        return {"name": self.name, "email": self.email, "asset_list": [a.to_dict() for a in self.asset_list]}

    @classmethod
    def from_dict(cls, d: dict):
        asset_list = [Asset.from_dict(a) for a in d["asset_list"]]
        return User(name=d["name"], email=d["email"], asset_list=asset_list)

