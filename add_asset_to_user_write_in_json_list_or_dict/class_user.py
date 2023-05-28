from add_asset_to_user_write_in_json_list_or_dict.class_asset import Asset


class User:
    def __init__(self, id_: int, name: str, asset: list[Asset] = None):
        self.__id_ = id_
        self.__name = name
        self.__asset = asset if asset else []

    @property
    def id_(self):
        return self.__id_

    @property
    def name(self):
        return self.__name

    @property
    def asset(self):
        return self.__asset

    def to_dict(self) -> dict:
        return {
            "id_": self.id_,
            "name": self.name,
            "asset": [a.to_dict() for a in self.asset],
        }

    @classmethod
    def from_dict(cls, d: dict):
        return User(
            id_=d["id_"], name=d["name"], asset=[Asset.from_dict(a) for a in d["asset"]]
        )

    def to_tuple(self) -> tuple:
        asset_tuple = [a.to_tuple() for a in self.asset]
        return self.id_, self.name, asset_tuple

    @classmethod
    def from_tuple(cls, info: tuple):
        asset_obj = [Asset.from_tuple(a) for a in info[2]]
        return User(id_=info[0], name=info[1], asset=asset_obj)
