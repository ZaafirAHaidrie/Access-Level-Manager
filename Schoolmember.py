from records import student_records


class SchoolMember:
    def __init__(self, full_name, id_number):
        self.full_name = full_name
        self.id_number = id_number
        self.position = "Member"

    def display(self):
        print(f"{self.position}: {self.full_name} (ID {self.id_number})")

    def list_students(self):
        print("\nStudents:")
        for student in student_records:
            print(f"{student['id']} - {student['full_name']} - {student['grade']}")

    def deny(self, action):
        print(f"{self.position} is not permitted to {action}")