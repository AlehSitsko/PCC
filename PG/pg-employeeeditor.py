# basic program to add,store, edit employee details and display them
employee_data = {}
def add_employee(emp_id, name, position):
    employee_data[emp_id] = {'name': name, 'position': position}
    print(f"Employee {name} added successfully.")
def edit_employee(emp_id, name=None, position=None):
    if emp_id in employee_data:
        if name:
            employee_data[emp_id]['name'] = name
        if position:
            employee_data[emp_id]['position'] = position
        print(f"Employee {emp_id} updated successfully.")
    else:
        print(f"Employee ID {emp_id} not found.")
def display_employees():
    if employee_data:
        print("Employee Details:")
        for emp_id, details in employee_data.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Position: {details['position']}")
    else:
        print("No employee data available.")
# loop to interact with the user
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Edit Employee")
    print("3. Display Employees")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        add_employee(emp_id, name, position)
    elif choice == '2':
        emp_id = input("Enter Employee ID to edit: ")
        name = input("Enter new name (leave blank to keep current): ")
        position = input("Enter new position (leave blank to keep current): ")
        edit_employee(emp_id, name if name else None, position if position else None)
    elif choice == '3':
        display_employees()
    elif choice == '4':
        print("Exiting Employee Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
# End of program