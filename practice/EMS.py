class Employee:
    def __init__(self, emp_id, name, department):
        self.__emp_id = emp_id
        self.__name = name
        self.__department = department
        self.__attendance = []

    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_attendance(self):
        return self.__attendance

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def mark_attendance(self, date, status):
        self.__attendance.append((date, status))

    def show_details(self):
        print("ID:", self.__emp_id)
        print("Name:", self.__name)
        print("Department:", self.__department)

employees = {}

def add_employee():
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    emp = Employee(emp_id, name, department)  
    employees[emp_id] = emp
    print("Employee added successfully.")

def mark_attendance():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        date = input("Enter Date (DD-MM-YYYY): ")
        status = input("Enter Status (Present/Absent): ")
        employees[emp_id].mark_attendance(date, status)
        print("Attendance marked.")
    else:
        print("Employee not found.")

def view_employee():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        employees[emp_id].show_details()
    else:
        print("Employee not found.")

def view_attendance():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        attendance = employees[emp_id].get_attendance()
        print("Attendance Record:")
        for date, status in attendance:
            print(f"{date}: {status}")
    else:
        print("Employee not found.")

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Mark Attendance")
    print("3. View Employee Details")
    print("4. View Attendance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        mark_attendance()
    elif choice == '3':
        view_employee()
    elif choice == '4':
        view_attendance()
    elif choice == '5':
        print("Exiting Program.")
        break
    else:
        print("Invalid choice. Try again.")

