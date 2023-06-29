from api_ex.domain.user import User


class NotRightLength(Exception):
    pass


class NotValidEmail(Exception):
    pass


class UserFactory:
    @classmethod
    def create_user(cls, username: str, email: str) -> User:
        cls.__validate_username(username)
        cls.__validate_email(email)
        return User(username, email)

    @classmethod
    def __validate_username(cls, username: str):
        if not 6 <= len(username) <= 20:
            raise NotRightLength("Username must be between 6 and 20 chars")

    @classmethod
    def __validate_email(cls, email: str):
        if "@" not in email:
            raise NotValidEmail("Email must contain symbol @")

    @classmethod
    def from_tuple(cls, info: tuple):
        return User(username=info[0], email=info[1])
