from abc import ABC, abstractmethod


class EntertainmentStuff(ABC):
    def __init__(self, name: str, studio: str, total: float, consumed: float = 0):
        # super().__init__()
        self.name = name
        self.__studio = studio
        self.__total = total
        self.__consumed = consumed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) == str:
            self.__name = name
        else:
            self.__name = "not set"

    def add_time(self, minutes: float):
        self.__consumed += minutes

    @property
    def completion_percent(self) -> int:
        return int(self.__consumed / self.__total * 100)

    @staticmethod
    @abstractmethod
    def create_from_dict(d: dict):
        pass

    def to_dict(self):
        return {
            "name": self.name,
            "studio": self.__studio,
            "total": self.__total,
            "consumed": self.__consumed,
            "type": self.type,
        }

    @property
    def type(self) -> str:
        return self.__class__.__name__
