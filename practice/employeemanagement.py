class EmployeeManagement:
    def __init__(self, employee_id, name, department, designation, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_designation(self):
        return self.designation

    def set_designation(self, designation):
        self.designation = designation

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def increment_salary(self, amount):
        self.salary += amount
        print(f"Salary updated. New salary: ₹{self.salary}")

    def display_employee_details(self):
        print("Employee Details:")
        print(f"ID         : {self.employee_id}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.department}")
        print(f"Designation: {self.designation}")
        print(f"Salary     : ₹{self.salary}")

    def change_department(self, new_department):
        print(f"Department changed from {self.department} to {new_department}")
        self.department = new_department


emp1 = EmployeeManagement(113421, "John Cena", "IT", "IT Engineer", 55000)
emp2 = EmployeeManagement(145202, "Jane Smith", "HR", "HR Manager", 60000)

emp1.display_employee_details()
emp1.increment_salary(5000)
emp1.change_department("Data Science")
emp1.display_employee_details()

emp2.display_employee_details()
