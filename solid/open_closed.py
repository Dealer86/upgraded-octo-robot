# Open-Closed Principle
# Create a class Employee with a method calculate_salary() that returns the salary of the employee
# Implement the Open-Closed Principle by creating subclasses HourlyEmployee
# and SalariedEmployee that override the calculate_salary() method to
# calculate salary of their respective employees.


class Employee:
    def __init__(self, name: str, years: int):
        self.years = years
        self.__name = name

    def set_days_worked(self, days):
        self.days_worked = days

    def calculate_salary(self) -> float:
        return self.days_worked * (self.years * 100)


class HourlyEmployee(Employee):
    def __init__(self, name: str, years: int, hours: float):
        self.__hours = hours
        super().__init__(name, years)

    def calculate_salary(self) -> float:
        return self.days_worked * (self.years * 100) * (self.__hours / 8)


he = HourlyEmployee("adi", 1, 7)
he.set_days_worked(10)
print(he.calculate_salary())
