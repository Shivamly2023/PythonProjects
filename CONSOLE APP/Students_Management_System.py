students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        students[name] = {
            "Age": age,
            "Marks": marks
        }

        print("Student Added Successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No Students Found!")
        else:
            print("\n===== STUDENT LIST =====")
            for name, details in students.items():
                print(f"Name: {name}")
                print(f"Age: {details['Age']}")
                print(f"Marks: {details['Marks']}")
                print("-" * 25)

    # Search Student
    elif choice == "3":
        name = input("Enter Student Name: ")

        if name in students:
            print(f"Age: {students[name]['Age']}")
            print(f"Marks: {students[name]['Marks']}")
        else:
            print("Student Not Found!")


    # Update Marks
    elif choice == "4":
        name = input("Enter Student Name: ")

        if name in students:
            new_marks = float(input("Enter New Marks: "))
            students[name]["Marks"] = new_marks
            print("Marks Updated Successfully!")
        else:
            print("Student Not Found!")

    # Delete Student
    elif choice == "5":
        name = input("Enter Student Name: ")

        if name in students:
            del students[name]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    # Show Topper
    elif choice == "6":
        if len(students) == 0:
            print("No Students Found!")
        else:
            topper = max(students, key=lambda x: students[x]["Marks"])
            print("\n🏆 TOPPER")
            print("Name :", topper)
            print("Marks:", students[topper]["Marks"])

    # Exit
    elif choice == "7":
        print("Thank You!")
        'break'

    else:
        print("Invalid Choice!")
