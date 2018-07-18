class Employee:
    def __init__(self, name, emp_id):
        self.__name = name
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def get_name(self, name):
        return self.__name
    def get_emp_id(self, emp_id):
        return self.__emp_id

    def __str__(self):
        return "Name: " + self.__name + \
        "\nEmployee ID: " + self.__emp_id

class ProductionWorker(Employee):
    def __init__(self, name, emp_id, shift_num, hrly_pay):
        Employee.__init__(self, name, emp_id)
        self.__shift_num = shift_num
        self.__hrly_pay = hrly_pay

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num
    def set_hrly_pay(self, hrly_pay):
        self.__hrly_pay = hrly_pay

    def get_shift_num(self, shift_num):
        return self.__shift_num
    def get_hrly_pay(self, hrly_pay):
        return self.__hrly_pay
    def __str__(self):
        return Employee.__str__(self) + \
        "\nShift: " + self.__shift_num + \
        "\nTotal hourly pay: $" + self.__hrly_pay

class ShiftSupervisor(Employee):
    def __init__(self, name, emp_id, salary, bonus):
        Employee.__init__(self, name, emp_id)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary
    def set_bonus(self, bonus):
        self.__bonus = salary

    def get_salary(self, salary):
        return self.__salary
    def get_bonus(self, bonus):
        return self.__bonus

    def __str__(self):
        return Employee.__str__(self) + \
        "\nSalary: $" + self.__salary + \
        "\nEntitled bonus: $" + self.__bonus
