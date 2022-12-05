# This class represents the temporal employee

from Employee import Employee


class TemporalEmployee:

    def __init__(self, hourly_salary, number_of_hours_worked):
        self.hourly_salary = hourly_salary,
        self.number_of_hours_worked = number_of_hours_worked


class Sellers(TemporalEmployee): # sellers class is defined from the parent class Temporal_employee
    def __init__(self, sold_volume, commission):
        self.sold_volume = sold_volume,
        self.commission = commission


# The salary of temporal employee depends on the number of sales made

def hourly_paid(self, wage):
    wage = Employee.wage_of_employee
    if self.number_of_hours_worked > 24:
        return 24 * wage + (self.number_of_hours_worked - 24) * wage * 1.5
    else:
        return self.number_of_hours_worked * wage


def percentage_commission(self):
    if Employee == Sellers:
        self.sold_volume = 0
        percentage_sold = float(self.sold_volume / self.commission)
        return str(percentage_sold) + "%"

