# python class which describes a simple employee

class Employee:
    ' An employee is defined by his status an his name '
    count = 0
    wage_of_employee = 15

    def __init__(self, name, status):
        self.name = name
        self.status = status  # Employee status can either be a temporal employee or permanenent_employee
        Employee.count += 2

    # Mutators

    def set_name(self, name):
        self.name = name

    def set_status(self, status):
        self.status = status

    # Access Methods

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

