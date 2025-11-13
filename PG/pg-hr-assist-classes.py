from dataclasses import dataclass, field
from typing import List


# ============================
#   DATA CLASSES
# ============================

@dataclass
class Certification:
    name: str
    issued_by: str
    valid_until: str  # later can become a date object


@dataclass
class Employee:
    id: int
    name: str
    position: str
    certifications: List[Certification] = field(default_factory=list)


# ============================
#   INPUT HELPERS
# ============================

def input_certifications() -> List[Certification]:
    """Interactive input for certifications."""
    certifications: List[Certification] = []

    while True:
        add = input("\nAdd certification? (y/n): ").strip().lower()
        if add != "y":
            break

        cert_name = input("  Certification name: ").strip()
        issued_by = input("  Issued by: ").strip()
        valid_until = input("  Valid until (YYYY-MM-DD): ").strip()

        certifications.append(
            Certification(
                name=cert_name,
                issued_by=issued_by,
                valid_until=valid_until,
            )
        )

    return certifications


def create_employee_from_input(emp_id: int) -> Employee:
    """Create a new employee from user input with auto-generated ID."""

    print("\nChoose employee type / position:")
    print("1 - EMT")
    print("2 - Paramedic")
    print("3 - EVOC Driver")
    print("4 - EMR")
    print("5 - Other (manual position)")

    choice = input("Enter choice (1-5): ").strip()

    name = input("Enter employee name: ").strip()

    if choice == "1":
        position = "EMT"
    elif choice == "2":
        position = "Paramedic"
    elif choice == "3":
        position = "EVOC Driver"
    elif choice == "4":
        position = "EMR"
    elif choice == "5":
        position = input("Enter custom position title: ").strip()
    else:
        raise ValueError("Invalid employee type choice.")

    print(f"\nNow enter certifications for {name} ({position}):")
    certs = input_certifications()

    return Employee(
        id=emp_id,
        name=name,
        position=position,
        certifications=certs,
    )


# ============================
#   ID GENERATOR
# ============================

def get_next_employee_id(employees: List[Employee]) -> int:
    """Auto-increment employee ID based on current list."""
    if not employees:
        return 1
    return max(emp.id for emp in employees) + 1


# ============================
#   DISPLAY
# ============================

def print_employee(employee: Employee) -> None:
    """Pretty-print employee information."""
    print(f"ID: {employee.id}")
    print(f"Name: {employee.name}")
    print(f"Position: {employee.position}")

    if not employee.certifications:
        print("Certifications: none")
    else:
        print("Certifications:")
        for cert in employee.certifications:
            print(f"  • {cert.name} ({cert.issued_by}), valid until {cert.valid_until}")


# ============================
#   MAIN LOOP
# ============================

def main():
    employees: List[Employee] = []

    while True:
        try:
            next_id = get_next_employee_id(employees)
            new_employee = create_employee_from_input(next_id)
            employees.append(new_employee)

            print(f"\nEmployee added successfully! (ID: {next_id})")

        except ValueError as e:
            print(f"Error: {e}")

        again = input("\nAdd another employee? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n=== Final list of employees ===")
    for emp in employees:
        print("\n-----------------")
        print_employee(emp)

    print("\nProgram finished.")


if __name__ == "__main__":
    main()
