# class to represent a permanent employee
from Employee import Employee


class PermanentEmployee:

    def __init__(self, number_of_days, month_salary, number_of_children, marital_status, monthly_bonus):
        self.number_of_days = number_of_days,
        self.monthly_salary = month_salary,
        self.number_of_children = number_of_children,
        self.marital_status = marital_status,
        self.monthly_bonus = monthly_bonus

    def salary(self, salary):
        if self.number_of_days == 20:

            if self.marital_status:
                salary = sum(self.monthly_salary + self.monthly_bonus)

            else:
                salary = sum(self.monthly_salary)

            # Since no method is declared the monthly per children wage the method would be just be ignored
        salary = salary
        return str(salary) + "francs"

    def cumulSalary(self, cumulated_salary, number_of_days, monthly_salary, monthly_bonus):
        number_of_days = self.number_of_days
        monthly_salary = self.monthly_salary
        monthly_bonus = self.monthly_bonus
        cumulated_salary = (number_of_days * sum(monthly_salary, monthly_bonus))/20

        return str(cumulated_salary) + "francs"
