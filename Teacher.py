from records import student_records
from Schoolmember import SchoolMember
from Helpers import find_student


class Teacher(SchoolMember):
    def __init__(self, full_name, id_number, department):
        super().__init__(full_name, id_number)
        self.position = "Teacher"
        self.department = department

    def list_students(self):
        print(f"\nStudents ({self.department} class):")
        for student in student_records:
            print(f"{student['id']} - {student['full_name']} - {student['grade']} - "
                  f"Score {student['score']} - Presence {student['presence']}%")

    def update_marks(self, sid, score):
        student = find_student(sid)
        if student:
            student["score"] = score
            print(f"Updated score for {student['full_name']} to {score}")
        else:
            print(f"No student found with ID {sid}")

    def update_attendance(self, sid, presence):
        student = find_student(sid)
        if student:
            student["presence"] = presence
            print(f"Updated attendance for {student['full_name']} to {presence}%")
        else:
            print(f"No student found with ID {sid}")

    def list_teachers(self):
        self.deny("list teachers")

    def register_student(self, *ignored):
        self.deny("register students")

    def remove_student(self, *ignored):
        self.deny("remove students")