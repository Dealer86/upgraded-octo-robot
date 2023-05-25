
from email_validator import validate_email, EmailNotValidError

from API_which_can_save_users.domain.user import User


class UsernameNotValid(Exception):
    pass


class EmailNotValid(Exception):
    def __init__(self, email: str):
        super().__init__(f"Email {email} not valid. Needs to have @ and .")


class UserFactory:
    @classmethod
    def create(cls, name: str, email: str) -> User:
        cls.validate_username(name)
        cls.validate_email(email)
        return User(name, email)

    @classmethod
    def validate_username(cls, name: str):
        if not 6 < len(name) < 20:
            raise UsernameNotValid("Username must be above 6 chars")

    @classmethod
    def validate_email(cls, email: str):
        if not validate_email(email):
            raise EmailNotValidError()

    @classmethod
    def create_from_db(cls, info: tuple) -> User:
        return User(id_=info[0], name=info[1], email=info[2])
