def teacher_menu(user):
    while True:
        print("\n1. View Students\n2. Update Marks\n3. Update Attendance\n4. View Teachers\n5. Register Student\n6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            user.list_students()
        elif choice == "2":
            sid = int(input("Student ID: "))
            score = int(input("New score: "))
            user.update_marks(sid, score)
        elif choice == "3":
            sid = int(input("Student ID: "))
            presence = int(input("New attendance: "))
            user.update_attendance(sid, presence)
        elif choice == "4":
            user.list_teachers()
        elif choice == "5":
            user.register_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


def principal_menu(user):
    while True:
        print("\n1. View Students\n2. View Teachers\n3. School Summary\n4. Register Student\n5. Set Pay\n6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            user.list_students()
        elif choice == "2":
            user.list_teachers()
        elif choice == "3":
            user.summary()
        elif choice == "4":
            user.register_student()
        elif choice == "5":
            user.set_pay()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


def admin_menu(user):
    while True:
        print("\n1. View Students\n2. View Teachers\n3. Register Student\n4. Modify Student\n5. Remove Student"
              "\n6. Register Teacher\n7. Set Pay\n8. Remove Teacher\n9. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            user.list_students()
        elif choice == "2":
            user.list_teachers()
        elif choice == "3":
            sid = int(input("New student ID: "))
            full_name = input("Full name: ")
            grade = input("Grade: ")
            score = int(input("Score: "))
            presence = int(input("Presence: "))
            user.register_student(sid, full_name, grade, score, presence)
        elif choice == "4":
            sid = int(input("Student ID: "))
            field = input("Field to update: ")
            value = input("New value: ")
            user.modify_student(sid, field, value)
        elif choice == "5":
            sid = int(input("Student ID: "))
            user.remove_student(sid)
        elif choice == "6":
            tid = int(input("New teacher ID: "))
            full_name = input("Full name: ")
            department = input("Department: ")
            pay = int(input("Pay: "))
            user.register_teacher(tid, full_name, department, pay)
        elif choice == "7":
            tid = int(input("Teacher ID: "))
            pay = int(input("New pay: "))
            user.set_pay(tid, pay)
        elif choice == "8":
            tid = int(input("Teacher ID: "))
            user.remove_teacher(tid)
        elif choice == "9":
            break
        else:
            print("Invalid choice")