from records import student_records, teacher_records
from Schoolmember import SchoolMember
from Helpers import find_student, find_teacher


class Admin(SchoolMember):
    def __init__(self, full_name, id_number):
        super().__init__(full_name, id_number)
        self.position = "Admin"

    def list_students(self):
        print("\nStudents (Admin view):")
        for student in student_records:
            print(student)

    def list_teachers(self):
        print("\nStaff (Admin view):")
        for teacher in teacher_records:
            print(teacher)

    def register_student(self, sid, full_name, grade, score=0, presence=0):
        student_records.append({"id": sid, "full_name": full_name, "grade": grade,
                                 "score": score, "presence": presence})
        print(f"Registered student {full_name} with ID {sid}")

    def modify_student(self, sid, field, value):
        student = find_student(sid)
        if student and field in student:
            student[field] = value
            print(f"Updated {field} for {student['full_name']} to {value}")
        else:
            print(f"Update failed")

    def remove_student(self, sid):
        student = find_student(sid)
        if student:
            student_records.remove(student)
            print(f"Removed student {student['full_name']} with ID {sid}")
        else:
            print(f"Removal Failed")

    def register_teacher(self, tid, full_name, department, pay):
        teacher_records.append({"id": tid, "full_name": full_name, "department": department, "pay": pay})
        print(f"Registered teacher {full_name} with ID {tid}")

    def set_pay(self, tid, pay):
        teacher = find_teacher(tid)
        if teacher:
            teacher["pay"] = pay
            print(f"Updated pay for {teacher['full_name']} to {pay}")
        else:
            print("Update failed")

    def remove_teacher(self, tid):
        teacher = find_teacher(tid)
        if teacher:
            teacher_records.remove(teacher)
            print(f"Removed teacher {teacher['full_name']} with ID {tid}")
        else:
            print("Removal failed")