from Helpers import teachersearch
from Teacher import Teacher
from Principal import Principal
from Admin import Admin


def login():
    print("Who is viewing?")
    print("1. Teacher")
    print("2. Principal")
    print("3. Admin")
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        teacherid = int(input("Enter your Teacher ID: "))
        teacher = teachersearch(teacherid)
        if teacher:
            return Teacher(teacher["full_name"], teacher["id"], teacher["department"])
        else:
            print(f"No teacher found with ID {teacherid}")
            return None
    elif choice == "2":
        return Principal("Mr. Shahzad", 201)
    elif choice == "3":
        return Admin("Head Admin", 901)
    else:
        print("Invalid choice")
        return None