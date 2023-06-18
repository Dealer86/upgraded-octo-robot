# Open Closed Principle - A class/function should be open to extension but close to change.

class StorageLocker:
    def authenticate(self, client):
        if client == "aws":
            pass
        elif client == "azure":
            pass
        elif client == "google cloud":
            pass
        return client

    def upload(self, filename, client):
        if client == "aws":
            pass
        elif client == "azure":
            pass


from abc import ABC, abstractmethod


class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class Uploader(ABC):
    @abstractmethod
    def upload_file(self):
        pass


class Aws(Auth, Uploader):
    def authenticate(self):
        pass
    def upload_file(self):
        pass


class Azure(Auth, Uploader):
    def authenticate(self):
        pass
    def upload_file(self):
        pass