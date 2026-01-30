def add_student(records, student_id, name, major, gpa):
    """Adds a new student to the records dictionary."""
    student_details = {
        "name": name,
        "major": major,
        "gpa": gpa
    }
    records[student_id] = student_details
    print(f"Student {name} (ID: {student_id}) added.")

def view_student(records, student_id):
    """Retrieves and displays details for a specific student ID."""
    if student_id in records:
        student = records[student_id]
        print(f"\n--- Student Details for ID: {student_id} ---")
        print(f"Name: {student['name']}")
        print(f"Major: {student['major']}")
        print(f"GPA: {student['gpa']:.2f}")
    else:
        print(f"Student ID '{student_id}' not found.")

def update_gpa(records, student_id, new_gpa):
    
    if student_id in records:
        records[student_id]["gpa"] = new_gpa
        print(f"GPA for Student ID '{student_id}' updated to {new_gpa:.2f}.")
    else:
        print(f"Student ID '{student_id}' not found. Cannot update GPA.")

def list_all_students(records):
    
    if not records:
        print("No student records available.")
        return

    print("\n--- All Student Records ---")
    for s_id, details in records.items():
        print(f"ID: {s_id}, Name: {details['name']}, Major: {details['major']}, GPA: {details['gpa']:.2f}")
    print("---------------------------")

def main():
    #main loop
    student_records = {}

    while True:
        print("\n--- Student Record Menu ---")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update GPA")
        print("4. List All Students")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            s_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            major = input("Enter Student Major: ").strip()
            try:
                gpa = float(input("Enter Student GPA: "))
                add_student(student_records, s_id, name, major, gpa)
            except ValueError:
                print("Invalid input. GPA must be a number.")

        elif choice == '2':
            s_id = input("Enter Student ID to view: ").strip()
            view_student(student_records, s_id)

        elif choice == '3':
            s_id = input("Enter Student ID to update: ").strip()
            try:
                new_gpa = float(input("Enter new GPA: "))
                update_gpa(student_records, s_id, new_gpa)
            except ValueError:
                print("Invalid input. GPA must be a number.")

        elif choice == '4':
            list_all_students(student_records)

        elif choice == '5':
            print("Exiting Student Record System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()