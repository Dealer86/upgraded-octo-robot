# Let's say you have a User class that currently handles user authentication and user profile management.
# This violates the SRP because the class has two distinct responsibilities.
class User1:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        # Code to authenticate the user
        pass

    def change_password(self, new_password):
        # Code to change the user's password
        pass

    def update_profile(self, profile_data):
        # Code to update the user's profile
        pass
# ---------------------------------------------------------------------------------


class Authenticator:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        if (len(self.username) and len(self.password)) < 3:
            raise Exception("Must be above 3")
        else:
            return "Valid username and password"


class UserPasswordManager:
    def __init__(self, password):
        self.password = password

    def change_password(self, new_password):
        if len(new_password) < 3:
            raise Exception("The new password must be at least 3 characters long.")
        else:
            self.password = new_password
            return self.password

    def update_profile(self, profile_data):
        # Code to update the user's profile
        pass


class User:
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.authenticator = Authenticator(self.username, self.password)
        self.profile_manager = UserPasswordManager(self.password)

    def authenticate(self):
        return self.authenticator.authenticate()

    def change_password(self, new_password):
        self.password = self.profile_manager.change_password(new_password)

    def update_profile(self, data_profile):
        self.profile_manager.update_profile(data_profile)


user1 = User("adil", "toa")
print(user1.authenticate())
print(user1.change_password("teodora"))
print(user1.password)
