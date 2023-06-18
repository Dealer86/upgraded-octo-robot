# This code breaks SRP
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def save_to_database(self):
        # Code to save employee data to the database
        pass

    def generate_report(self):
        # Code to generate a report based on employee data
        pass

    def send_email_notification(self):
        # Code to send an email notification to the employee
        pass


# ----------------------------------------------

class SaveEmployee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.employee_list = []

    def save_to_database(self):
        self.employee_list.append([self.name, self.age, self.salary])


class GenerateReport:

    def generate_report(self):
        # Code to generate a report based on employee data
        pass


class SendEmail:
    def send_email_notification(self):
        # Code to send an email notification to the employee
        pass


class Employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.save_employee = SaveEmployee(self.name, self.age, self.salary)
        self.generate_report = GenerateReport()
        self.send_email = SendEmail()

    def save_employees(self):
        self.save_employee.save_to_database()
        return self.save_employee.employee_list

    def generate_reports(self):
        self.generate_report.generate_report()

    def send_emails(self):
        self.send_email.send_email_notification()


emp = Employee1("adi", 36, 10000)
emp.save_employees()
print(emp.save_employee.employee_list)




