from records import student_records, teacher_records
from Schoolmember import SchoolMember


class Principal(SchoolMember):
    def __init__(self, full_name, id_number):
        super().__init__(full_name, id_number)
        self.position = "Principal"

    def list_students(self):
        print("\nStudents (Principal view):")
        for student in student_records:
            print(f"{student['id']} - {student['full_name']} - {student['grade']} - "
                  f"Score {student['score']} - Presence {student['presence']}%")

    def list_teachers(self):
        print("\nTeachers:")
        for teacher in teacher_records:
            print(f"{teacher['id']} - {teacher['full_name']} - {teacher['department']}")

    def summary(self):
        count_students = len(student_records)
        count_teachers = len(teacher_records)
        average_score = sum(student["score"] for student in student_records) / count_students
        average_attendance = sum(student["presence"] for student in student_records) / count_students
        print("\nSchool Summary:")
        print(f"Students: {count_students}, Teachers: {count_teachers}")
        print(f"Average Score: {average_score:.1f}")
        print(f"Average Attendance: {average_attendance:.1f}%")

    def register_student(self, *ignored):
        self.deny("register students")

    def set_pay(self, *ignored):
        self.deny("change staff pay")