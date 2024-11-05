class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Payroll:
    def __init__(self):
        self.employees = []  # List to s

    def add_employee(self, employee):
    
        self.employees.append(employee)

    def calculate_total_payroll(self):
        """Calculates the total payroll cost by summing the salaries of all employees."""
        return sum(employee.salary for employee in self.employees)


# Example usage
payroll = Payroll()

# Adding employees to the payroll
emp1 = Employee("Joseph", 1000)
emp2 = Employee("Habiba", 2000)
emp3 = Employee("Bob", 40000)

payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

# Calculate total payroll
total_payroll = payroll.calculate_total_payroll()
print(f"Total Payroll: {total_payroll}")

# Printing employee details
for employee in payroll.employees:
    print(f"Employee Name: {employee.name}, Salary: {employee.salary}")
