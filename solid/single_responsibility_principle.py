# Single responsibility principle
# Create a class logger that has only one responsibility: writing lg messages to a file.
# Make sure the class is easily reusable
# logger methods receive a text and writes it to the file
# It also adds the current time % lo level(debug, info, warrning, error)
import datetime


class Logger:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def logger(self, message: str, level: str = "debug"):
        date = datetime.datetime.now()
        log_message = "\n" + f"{date}, {level}: {message} "
        with open(self.__file_path, "a") as f:
            f.write(log_message)

    def info(self, message):
        self.logger(message, "info")

    def error(self, message):
        self.logger(message, "error")
    

if __name__ == "__main__":
    log = Logger("1.log")
    log.logger("ceva n-a mers bine", "critical")
    log.info("iar nu a mers")





