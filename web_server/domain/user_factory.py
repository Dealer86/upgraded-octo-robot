from web_server.domain.user import User


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
            raise UsernameNotValid("Username must be above 5 chars")

    @classmethod
    def validate_email(cls, email: str):
        if "@" not in email and not email.count(".") == 1:
            raise EmailNotValid(email)
