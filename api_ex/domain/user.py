class User:
    def __init__(self, username: str, email: str):
        self.__username = username
        self.__email = email

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email
