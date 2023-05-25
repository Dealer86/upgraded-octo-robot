class User:
    def __init__(self, name: str, email: str, films: list[str] = None, shows: list[str] = None, id_: int = None):
        self.__name = name
        self.__email = email
        self.__films = films if films else []
        self.__shows = shows if films else []
        self.__id = id_

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def films(self):
        return self.__films

    @property
    def shows(self):
        return self.__shows

    @property
    def id(self):
        return self.__id
