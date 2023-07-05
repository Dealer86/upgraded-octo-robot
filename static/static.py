class InvalidEmail(Exception):
    def __init__(self):
        super().__init__("E-mail is invalid!")


class WeakPassword(Exception):
    pass


class User:
    def __init__(self, email: str, password: str):
        self.__set_email(email)
        self.__set_password(password)

    @property
    def email(self) -> str:
        return self.__email

    @property
    def password(self) -> str:
        return self.__password

    @staticmethod
    def is_email_valid(email: str) -> bool:
        # User.is_password_strong("parol") -> how to call antoher static or class method

        return "@" in email and "." in email.split("@")[1]

    @classmethod
    def is_password_strong(cls, password: str) -> bool:
        # cls.is_email_valid("email") -> how to call another static method or class method
        return len(password) > 10

    def __set_password(self, password):
        if self.is_password_strong(password):
            self.__password = password
        else:
            raise WeakPassword()

    def __set_email(self, email):
        if User.is_email_valid(email):
            self.__email = email
        else:
            raise InvalidEmail()


if __name__ == "__main__":
    try:
        user1 = User("adrian@gmail.com", "strPasrd1")
        print(user1.email)
    except InvalidEmail as e:
        print("Nu am putut crea userul! Error: " + str(e))
    except WeakPassword:
        print("parola este slaba")
    except Exception as e:
        print("Eroare de cod: " + str(e))
    # except Exception as e:
    #  pass
    # this will never be executed, Exception is caught before
    print("hola!")
