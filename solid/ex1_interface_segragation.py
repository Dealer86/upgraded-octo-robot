from abc import ABC, abstractmethod

# Interface segragation principle - Classes should not depend on methods or attributes they don't use.
# If a class doesn't use particular methods or attributes, then those attributes and methods should be segregated
# into more specific classes


# class Printer(ABC):
#     @abstractmethod
#     def print(self, document):
#         pass
#
#     @abstractmethod
#     def fax(self, document):
#         pass
#
#     @abstractmethod
#     def scan(self, document):
#         pass
#
#
# class OldPrinter(Printer):
#     def print(self, document):
#         print(f"Printing {document} in black and white...")
#
#     def fax(self, document):
#         raise NotImplementedError("Fax functionality not supported")
#
#     def scan(self, document):
#         raise NotImplementedError("Scan functionality not supported")
#
#
# class ModernPrinter(Printer):
#     def print(self, document):
#         print(f"Printing {document} in color...")
#
#     def fax(self, document):
#         print(f"Faxing {document}...")
#
#     def scan(self, document):
#         print(f"Scanning {document}...")


# --------------------------------------------------------------------------


class Printer(ABC):
    @abstractmethod
    def print(self):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class OldPrinter1(Printer):
    def print(self):
        print(f"Printing...")


class NewPrinter(Printer, Fax, Scanner):
    def print(self):
        print(f"Printing...")

    def fax(self):
        print(f"Faxing...")

    def scan(self):
        print(f"Scanning...")


new_printer = NewPrinter()
