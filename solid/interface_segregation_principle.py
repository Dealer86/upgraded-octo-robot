# Interface Segregation Principle
# Create a class TemperatureConverter that converts temperature between Celsius, Fahrenheit and Kelvin
# Implement the Interface Segregation Principle by spliting the class into multiple interfaces:
# CelsiusConverter, FahConverter & KevinConverter
# with methods to convert to and from that temperature scale
# interface in python = abstract class with only abstract methods
from abc import ABC, abstractmethod


class CelsiusFahrenheitConvertor(ABC):
    @abstractmethod
    def convert_celsius_to_fahrenheit(self):
        pass

    @abstractmethod
    def convert_fahrenheit_to_celsius(self):
        pass


class TemperatureConvertor(CelsiusFahrenheitConvertor):

    def convert_celsius_to_fahrenheit(self):
        pass

    def convert_fahrenheit_to_celsius(self):
        pass

    def convert_celsius_to_kelvin(self):
        pass

    def convert_fahrenheit_to_kelvin(self):
        pass

    def convert_kelvin_to_celsius(self):
        pass

    def convert_kelvin_to_fahrenheit(self):
        pass


class Calendar:
    def __init__(self, temp_conv: CelsiusFahrenheitConvertor):
        self.conv = temp_conv

    def add_appointment(self, date):
        pass

    def get_appointment(self, date):
        t = self.conv.convert_celsius_to_fahrenheit()
        pass
