import employee
import pickle

print()
print()
print("Employee Management Software ver. 0.1.0")
print()
print()

EMPLOYEE_PICKLE_LAB11 = 'Employee_lab11.dat'
SUPERVISOR_PICKLE_LAB11 = 'Supervisor_lab11.dat'

def main():

    employee_menu = 1
    supervisor_menu = 2
    display_all = 3
    quit_program = 4

    employees_all = load_employees()
    supervisors_all = load_supervisors()

    choice = 0
    while choice != quit_program:
        display_main_menu()
        choice = int(input("Please enter your selection: "))
        print()

        if choice == employee_menu:
            employee_main(employees_all)
        elif choice == supervisor_menu:
            supervisor_main(supervisors_all)
        elif choice == display_all:

            for name in employees_all:
                print(employees_all.get(name))
                print()

            for name in supervisors_all:
                print(supervisors_all.get(name))
                print()

        elif choice > 4:
            print("ERROR: That is an invalid choice")


def display_main_menu():
    print("     MAIN MENU")
    print("1) Employee Database")
    print("2) Supervisor Database")
    print("3) Display All")
    print("4) Quit Program")
    print()

def employee_main(employees_all):

    search_emp = 1
    add_emp = 2
    modify_emp =3
    delete_emp = 4
    display_emp = 5
    return_main = 6

    choice = 0
    while choice != return_main:
        display_emp_menu()
        choice = int(input("Please enter your selection: "))
        print()

        if choice == search_emp:
            search_emp_fn(employees_all)
        elif choice == add_emp:
            add_emp_fn(employees_all)
        elif choice == modify_emp:
            modify_emp_fn(employees_all)
        elif choice == delete_emp:
            delete_emp_fn(employees_all)
        elif choice == display_emp:
            display_emp_fn(employees_all)
        elif choice > 6:
            print("ERROR: That is an invalid choice")

def load_employees():
    try:
        employee_file_start = open(EMPLOYEE_PICKLE_LAB11, 'rb')
        employee_dictionary = pickle.load(employee_file_start)
        employee_file_start.close()
    except IOError:
        employee_dictionary = {}
    return employee_dictionary

def display_emp_menu():
    print("     Employee Menu")
    print('1) Search employees')
    print('2) Add a new employee')
    print('3) Modify an existing employee')
    print('4) Delete an employee')
    print('5) Display all employees')
    print('6) Return to previous menu')
    print()

def search_emp_fn(employees_all):
    another = 'Y'
    while another.upper() == 'Y':
        name = input("Please enter the Employee's name: ")
        print(employees_all.get(name, 'ERROR: Not found'))
        print()
        print("Do you want to search another Employee?")
        another = input("'Y' or 'N': ")
        print()

def add_emp_fn(employees_all):

    another = 'Y'
    while another.upper() == 'Y':
        name = input("Please enter the Employee's name: ")

        if name not in employees_all:
            emp_id = input("Please enter the Employee's ID: ")
            employee1 = employee.Employee(name, emp_id)
            print("Please enter the worker's shift")
            shift_num = shift()
            hrly_pay = input("Please enter the Employee's hourly pay: $")
            worker = employee.ProductionWorker(name, emp_id, shift_num, hrly_pay)
            employees_all[name] = worker
            print("Employee successfully added")
        else:
            print("ERROR: Employee already exists")
            print()
        print('Do you want to add another Employee?')
        another = input('Y or N: ')
        print()

        save_pickle_emp(employees_all)

def shift():
    shift_num = int(input("Enter 1 for Day Shift or 2 for Night Shift: "))
    if shift_num == 1:
        return "Day Shift"
    elif shift_num == 2:
        return "Night Shift"
    elif shift_num > 2:
        print("ERROR: That is an invalid entry")

def modify_emp_fn(employees_all):
    another = 'Y'
    while another.upper() == 'Y':
        name = input("Please enter the Employee's name: ")

        if name in employees_all:
            emp_id = input("Please enter the Employee's new ID: ")
            employee1 = employee.Employee(name, emp_id)
            print("Please enter the worker's new shift")
            shift_num = shift()
            hrly_pay = input("Please enter the Employee's new hourly pay: $")
            worker = employee.ProductionWorker(name, emp_id, shift_num, hrly_pay)
            employees_all[name] = worker
            print("Employee successfully modified")
        else:
            print('ERROR: Employee not found')
        print()
        print('Do you want to modify another Employee?')
        another = input('Y or N: ')
        print()

        save_pickle_emp(employees_all)

def delete_emp_fn(employees_all):
    another = 'Y'
    while another == 'Y':
        name = input("Enter Employee's name: ")

        if name in employees_all:
            del employees_all[name]
            print("Employee entry successfully deleted")
        else:
            print('ERROR: Employee not found')
        print()
        print('Do you want to delete another entry?')
        another = input('Y or N: ')
        print()

    save_pickle_emp(employees_all)

def display_emp_fn(employees_all):

    for name in employees_all:
        print(employees_all.get(name))
        print()

def save_pickle_emp(employees_all):
    employee_file_end = open(EMPLOYEE_PICKLE_LAB11, 'wb')
    pickle.dump(employees_all, employee_file_end)
    employee_file_end.close()

def supervisor_main(supervisors_all):

    search_sup = 1
    add_sup = 2
    modify_sup =3
    delete_sup = 4
    display_sup = 5
    return_main = 6

    choice = 0
    while choice != return_main:
        display_sup_menu()
        choice = int(input("Please enter your selection: "))
        print()

        if choice == search_sup:
            search_sup_fn(supervisors_all)
        elif choice == add_sup:
            add_sup_fn(supervisors_all)
        elif choice == modify_sup:
            modify_sup_fn(supervisors_all)
        elif choice == delete_sup:
            delete_sup_fn(supervisors_all)
        elif choice == display_sup:
            display_sup_fn(supervisors_all)
        elif choice > 6:
            print("ERROR: That is an invalid choice")

def load_supervisors():
    try:
        supervisor_file_start = open(SUPERVISOR_PICKLE_LAB11, 'rb')
        supervisor_dictionary = pickle.load(supervisor_file_start)
        supervisor_file_start.close()
    except IOError:
        supervisor_dictionary = {}
    return supervisor_dictionary

def display_sup_menu():
    print("     Supervisor Menu")
    print('1) Search supervisors')
    print('2) Add a new supervisor')
    print('3) Modify an existing supervisor')
    print('4) Delete an supervisor')
    print('5) Display all supervisors')
    print('6) Return to previous menu')
    print()

def search_sup_fn(supervisors_all):
    another = 'Y'
    while another.upper() == 'Y':
        name = input("Please enter the Supervisor's name: ")
        print(supervisors_all.get(name, 'ERROR: Not found'))
        print()
        print("Do you want to search another Supervisor?")
        another = input("'Y' or 'N': ")
        print()

def add_sup_fn(supervisors_all):

    another = 'Y'
    while another.upper() == 'Y':
        name = input("Please enter the Supervisor's name: ")

        if name not in supervisors_all:
            emp_id = input("Please enter the Supervisor's ID: ")
            employee1 = employee.Employee(name, emp_id)
            salary = input("Please enter the Supervisor's salary: $")
            bonus = input("Please enter the Supervisor's entitled bonus: $")
            supervisor = employee.ShiftSupervisor(name, emp_id, salary, bonus)
            supervisors_all[name] = supervisor
            print("Supervisor successfully added")
        else:
            print("ERROR: Supervisor already exists")
            print()
        print('Do you want to add another Supervisor?')
        another = input('Y or N: ')
        print()

    save_pickle_sup(supervisors_all)

def modify_sup_fn(supervisors_all):
    another = 'Y'
    while another.upper() == 'Y':
        name = input("Please enter the Supervisor's name: ")

        if name in supervisors_all:
            emp_id = input("Please enter the Supervisor's new ID: ")
            employee1 = employee.Employee(name, emp_id)
            salary = input("Please enter the Supervisor's new salary: $")
            bonus = input("Please enter the Supervisor's new entitled bonus: $")
            supervisor = employee.ShiftSupervisor(name, emp_id, salary, bonus)
            supervisors_all[name] = supervisor
            print("Supervisor successfully modified")
        else:
            print('ERROR: Supervisor not found')
        print()
        print('Do you want to modify another Supervisor?')
        another = input('Y or N: ')
        print()

    save_pickle_sup(supervisors_all)

def delete_sup_fn(supervisors_all):
    another = 'Y'
    while another == 'Y':
        name = input("Enter Supervisor's name: ")

        if name in supervisors_all:
            del supervisors_all[name]
            print("Supervisor entry successfully deleted")
        else:
            print('ERROR: Supervisor not found')
        print()
        print('Do you want to delete another entry?')
        another = input('Y or N: ')
        print()

    save_pickle_sup(supervisors_all)

def display_sup_fn(supervisors_all):

    for name in supervisors_all:
        print(supervisors_all.get(name))
        print()

def save_pickle_sup(supervisors_all):
    supervisor_file_end = open(SUPERVISOR_PICKLE_LAB11, 'wb')
    pickle.dump(supervisors_all, supervisor_file_end)
    supervisor_file_end.close()

main()
