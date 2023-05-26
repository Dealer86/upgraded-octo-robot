from and_again.asset import Asset


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
        asset_dict = [u.to_dict() for u in self.asset]
        return {"id_": self.id_, "name": self.name, "asset": asset_dict}

    @classmethod
    def from_dict(cls, d: dict):
        return User(
            id_=d["id_"], name=d["name"], asset=[Asset.from_dict(a) for a in d["asset"]]
        )
