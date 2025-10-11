# Average salary calculator program
import math
# Sample employee data
employees = [
    {"name": "Alice", "salary": 3500},
    {"name": "Bob", "salary": 4200},
    {"name": "Charlie", "salary": 2800},
    {"name": "Diana", "salary": 5000}
]
# Function to calculate average salary and print min/max and average
def calculate_average_salary(employee_list):
    if not employee_list:
        print("No employees provided.")
        return
    salaries = [emp.get("salary", 0) for emp in employee_list if isinstance(emp, dict)]
    if not salaries:
        print("No valid salary data found.")
        return
    min_salary = min(salaries)
    max_salary = max(salaries)
    avg_salary = sum(salaries) / len(salaries)
    print(f"Minimum salary: {min_salary}")
    print(f"Maximum salary: {max_salary}")
    print(f"Average salary: {avg_salary:.2f}")

if __name__ == "__main__":
    calculate_average_salary(employees)