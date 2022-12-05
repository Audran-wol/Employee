from Employee import Employee
from Permanent_employee import PermanentEmployee
from Temporal_employee import TemporalEmployee
import mysql.connector

Employee = Employee()
PermanentEmployee = PermanentEmployee()
TemporalEmployee = TemporalEmployee()

con = mysql.connector.connect(
    host="localhost", use_pure="root", password="password", database="employee"
)

# Display the content of instance employee
print("There are %d employees" % Employee.count)
print("Name: ", Employee.name, "Status: ", Employee.status)

# Example
e1 = ("John", "Temporal_employee")
e2 = ("Mark", "Permanent_employee")


# Hire or add employ
def Hire_employee():

    Employee.status = PermanentEmployee or TemporalEmployee
    name = input("Enter Employees name: ")
    status = input("Is it for a temporal or permanent employ")
    if status == PermanentEmployee:
        marital_status = input("Are you maried: ")
        if marital_status:
            number_of_children = input("How many children do you have")
            return number_of_children
    else:
        seller = input("Dou you have a seller or just a simple temporal_employee")
        if seller:
            return seller
    data = (name, status)
    # Inserting Employee details in the Employee table
    sql = 'insert into employee values(%s, %s)'
    c = con.cursor()

    # Executing sql query
    c.execute(sql, data)

    con.commit()
    print("Employee added Succesfully")


Hire_employee()


# This function would be used to check employee with a given name after his hired
def check_employee(employee_name):

    # select employee from employee table
    sql = 'select * from employee where name=%s'

    # making cursor buffered to make
    # rowcount method properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    # executing the sql query
    c.execute(sql, data)

    # rowcount method to find
    r = c.rowcount

    if r == 1:
        return True
    else:
        return False


# To remove an employee we have to check in the list of created employees in sql table then dismiss the employee by his
# name so using the check_employee function  built above we can do it as such
def Dismiss_Employ():

    Name = input("Enter the employee name: ")

    # Checking if the employee is withing the list of employees
    if( check_employee(Name) == False):
        print("Employee does not exits\nTry again\n")

    else:
        sql = 'delete from employee where name=%s'
        data = (Name,)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # Commit method to make changes
        con.commit()
        print("Employee Dismiss")


Dismiss_Employ()


def Mute_employ():
    pass

# Methode mute employee not comprehensive