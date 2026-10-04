
# Review Programming Assignment
# Program Description: Employee Directory Program - Review Classes/Objects,
# Files Read/Write and Dictionaries
# Your Name: Sudhir Sah
# Date: October 3, 2026

# Employee Class
class Employee:
    """Employee class to keep track employee info"""

    def __init__(self, ID=-999, name='', department='', pay=0.0):
        """initializer for new employee object"""
        self.set_ID(ID)
        self.set_name(name)
        self.set_department(department)
        self.set_pay(pay)

    def get_ID(self):
        """return employee id"""
        return self.ID

    def set_ID(self, ID):
        """assign employee id"""
        self.ID = ID

    def get_name(self):
        """return employee name"""
        return self.name

    def set_name(self, name):
        """assign employee name"""
        self.name = name

    def get_department(self):
        """return employee department"""
        return self.department

    def set_department(self, department):
        """assign employee department"""
        self.department = department

    def get_pay(self):
        """return employee pay"""
        return self.pay

    def set_pay(self, pay):
        """assign employee pay"""
        self.pay = pay

    def __str__(self):
        """return employee object in string"""
        return f'{self.get_ID()}\t{self.get_name()}\t{self.get_department()}\t{self.get_pay()}'


class EmployeeDirectory:
    """Track employee info in the directory"""

    def __init__(self):
        """initialize employee_list and employee_dict"""
        self.employee_list = []
        self.employee_dict = {}

    def add_employee(self, employee):
        """append employee object to the employee_list"""
        if employee not in self.employee_list:
            self.employee_list.append(employee)

    def del_employee(self, employee):
        """delete employee object from the employee_list"""
        if employee in self.employee_list:
            self.employee_list.remove(employee)
        else:
            print(f'ID:{employee.get_ID()} does not exist, deletion is aborted')

    def read_file(self, file_name):
        """read employees.txt and return a list of employee objects"""
        employee_list = []

        with open(file_name, 'r') as infile:
            for line in infile:
                data = line.split()

                ID = int(data[0])
                name = data[1]
                department = data[2]
                pay = float(data[3])

                employee_list.append(Employee(ID, name, department, pay))

        return employee_list

    def update_employee_dir(self, file_name):
        """call read_file and update employee_list"""
        self.employee_list = self.read_file(file_name)

    def write_to_file(self, file_name):
        """write the updated employee_list to file"""
        with open(file_name, 'w') as outfile:
            for employee in self.employee_list:
                outfile.write(
                    f'{employee.get_ID()} '
                    f'{employee.get_name()} '
                    f'{employee.get_department()} '
                    f'{employee.get_pay()}\n'
                )

    def write_to_dict(self):
        """convert employee_list data to a dictionary of lists"""
        self.employee_dict = {
            'ID': [],
            'name': [],
            'department': [],
            'pay': []
        }

        for emp in self.employee_list:
            self.employee_dict['ID'].append(emp.get_ID())
            self.employee_dict['name'].append(emp.get_name())
            self.employee_dict['department'].append(emp.get_department())
            self.employee_dict['pay'].append(emp.get_pay())

    def display_dict(self):
        """display employee dictionary in key/value pairs"""
        for key, value in self.employee_dict.items():
            print(f'{key} : {value}')


if __name__ == '__main__':
    try:
        employee_dir = EmployeeDirectory()

        employee_dir.update_employee_dir('employees.txt')

        emp1 = Employee(106, 'Emp1', 'Accounting', 56000.0)
        emp2 = Employee(107, 'Emp2', 'Sales', 80000.0)
        emp3 = Employee(108, 'Emp3', 'Marketing', 90000.0)

        employee_dir.add_employee(emp1)
        employee_dir.add_employee(emp2)

        employee_dir.del_employee(emp3)

        employee_dir.write_to_file('employees.txt')
        employee_dir.write_to_dict()
        employee_dir.display_dict()

    except FileNotFoundError as fnfe:
        print(fnfe)
    except KeyError as ke:
        print(ke)
    except Exception as ex:
        print(ex)
    finally:
        print('Program is completed')
