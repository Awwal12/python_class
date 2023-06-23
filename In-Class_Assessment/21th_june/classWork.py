# Define a class called Employee with a construtor that takes a name and a salary...  The class should have a method called get_salary that returns the salary of the employee
# Define two subclasses of Employee called Manager and Engineer, that inherit from Employee and have their own bonus attribute .... The manager class should hve a bonus of 10% of the salary and the Engineer class should have a bonus of 5% of the salary... The subclasses should override the get_salary method to return the salary plus the bonus.
# Write a function called payroll that takes a list of employees and prints thier name and salary .
# Create a list of employees with different names and salaries and pass it to the payroll function.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus=0.1):
        Employee.__init__(self, name, salary)
        self.bonus = bonus

    def get_salary(self):
        self.val = (self.salary * self.bonus)
        self.salary += self.val
        return self.salary


class Engineer(Employee):
    def __init__(self, name, salary, bonus=0.05):
        Employee.__init__(self, name, salary)
        self.bonus = bonus

    def get_salary(self):
        self.val = (self.salary * self.bonus)
        self.salary += self.val
        return self.salary


def payroll(staffs):
    name_salary = {}
    for staff in staffs:
        if staffs[staff]["occupation"] == "engineer":
            profile = Engineer(staff, staffs[staff]["salary"])
        elif staffs[staff]["occupation"] == "manager":
            profile = Manager(staff, staffs[staff]["salary"])
        name_salary[profile.name] = int(profile.get_salary())
    print(name_salary)


payroll({
    "james": {"salary": 5000, "occupation": "engineer"},
    "john": {"salary": 6000, "occupation": "manager"},
    "mary": {"salary": 5000, "occupation": "manager"}
})
