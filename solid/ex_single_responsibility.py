# The SRP states that a class should have only one reason to change.
# In other words, a class should have a single responsibility or a single job to do.

# Here's an example to illustrate SRP in Python:

class FileManager1:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write_file(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

    def encrypt_file(self):
        # Code to encrypt the contents of the file
        pass

    def compress_file(self):
        # Code to compress the file
        pass


# In this example, we have a FileManager class that is responsible for reading and writing files,
# as well as encrypting and compressing files. However, this violates the SRP because the class
# has multiple responsibilities.
#
# Homework for SRP:
# Your homework is to refactor the FileManager class to adhere to the Single Responsibility Principle.
# Create separate classes for reading/writing files and encrypting/compressing files.
# Each class should have a single responsibility. Here's a suggested structure:
#
# Create a FileReader class that has the responsibility of reading files.
# Create a FileWriter class that has the responsibility of writing files.
# Create an Encryptor class that has the responsibility of encrypting files.
# Create a Compressor class that has the responsibility of compressing files.


class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_files(self, data):
        with open(self.filename, "w") as f:
            f.write(data)


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_files(self):
        with open(self.filename) as f:
            return f.read()


class Encryptor:
    def encrypt_files(self, data):
        pass


class Compressor:
    def compress_files(self, data):
        pass


class FileManager:
    def __init__(self):
        self.reader = FileReader("something.txt")
        self.writer = FileWriter("something.txt")
        self.encryptor = Encryptor()
        self.compressor = Compressor()

    def read_files(self):
        return self.reader.read_files()

    def write_files(self, data):
        self.writer.write_files(data)

    def encrypt_files(self):
        data = self.read_files()
        encrypt_data = self.encryptor.encrypt_files(data)
        self.write_files(encrypt_data)

    def compress_files(self):
        data = self.read_files()
        compress_data = self.compressor.compress_files(data)
        self.write_files(compress_data)





