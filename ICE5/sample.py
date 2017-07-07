class Employee(object):
    numOfEmp = 0
    def __init__(self):
        self.type = "Developer"

    def calculate(self):
        # to calculate number of employees
        self.numOfEmp += 1
        print("Number of employees:", self.numOfEmp)

    def display(self, name, sal):
        print("Employee Name:",name)
        print("Salary of the Employee:",sal)
        print("Designation of Employee:",self.type)

    def addEmployee(self, name, sal):
        self.display(name, sal)
        self.calculate()

employee = Employee()
employee.addEmployee('esha', 1000)
employee.addEmployee('mayuri', 2000)

class Manager(Employee):
    def __init__(self):
        self.type = "Manager"

manager = Manager()
manager.addEmployee('XXX', 5000)