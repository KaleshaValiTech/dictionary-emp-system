# Solution
employees = {}

def add_employee():
    emp_id = "E" + str(len(employees) + 101)
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    dept = input("Enter Department: ")

    if not name.isalpha() or not age.isdigit() or int(age) <= 0:
        print("Invalid input!")
        return

    employees[emp_id] = {"name": name, "age": int(age), "dept": dept}
    print(f"Employee {emp_id} added!")

def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    if employees.pop(emp_id, None):
        print("Employee removed!")
    else:
        print("ID not found!")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id in employees:
        name = input("Enter new Name (leave blank to keep): ") or employees[emp_id]["name"]
        age = input("Enter new Age (leave blank to keep): ") or employees[emp_id]["age"]
        dept = input("Enter new Department (leave blank to keep): ") or employees[emp_id]["dept"]
        
        if not name.isalpha() or not str(age).isdigit() or int(age) <= 0:
            print("Invalid input!")
            return

        employees[emp_id] = {"name": name, "age": int(age), "dept": dept}
        print("Employee updated!")
    else:
        print("ID not found!")

def search_employee():
    search = input("Enter Employee ID or Name: ").lower()
    found = [f"{k}: {v['name']}, Age: {v['age']}, Dept: {v['dept']}" 
             for k, v in employees.items() if search in k.lower() or search in v["name"].lower()]
    
    print("\n".join(found) if found else "No employee found!")

def sort_employees():
    key = input("Sort by (name/age/dept): ").lower()
    if key in {"name", "age", "dept"}:
        for k, v in sorted(employees.items(), key=lambda x: x[1][key]):
            print(f"{k}: {v['name']}, Age: {v['age']}, Dept: {v['dept']}")
    else:
        print("Invalid sort option!")

def main():
    actions = {"1": add_employee, "2": remove_employee, "3": update_employee, 
               "4": search_employee, "5": sort_employees}

    while True:
        choice = input("\n1. Add 2. Remove 3. Update 4. Search 5. Sort 6. Exit\nChoose: ")
        if choice == "6":
            print("Goodbye!"); break
        actions.get(choice, lambda: print("Invalid choice!"))()

main()
