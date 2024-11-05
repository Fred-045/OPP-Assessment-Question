class Employee:
    def calculate_salary(self):
        print('This is calculation for employee')
class manager(Employee):
    def culculate_salary(self):
        basic_salary = 350000
        allowance =5000
        total_salary = basic_salary + allowance
        print(f"Total Manager Salary: ksh{total_salary}")

employee = Employee()
employee.calculate_salary()  # Calls the method in the Employee class

manager = manager()
manager.calculate_salary()   