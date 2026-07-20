from Schoolmember import SchoolMember
from Helpers import find_student, find_teacher, get_all_students, get_all_teachers
from database import get_connection

ALLOWED_STUDENT_FIELDS = {"full_name", "grade", "score", "presence"}


class Admin(SchoolMember):
    def __init__(self, full_name, id_number):
        super().__init__(full_name, id_number)
        self.position = "Admin"

    def list_students(self):
        print("\nStudents (Admin view):")
        for student in get_all_students():
            print(student)

    def list_teachers(self):
        print("\nStaff (Admin view):")
        for teacher in get_all_teachers():
            print(teacher)

    def register_student(self, sid, full_name, grade, score=0, presence=0):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (id, full_name, grade, score, presence) VALUES (?, ?, ?, ?, ?)",
            (sid, full_name, grade, score, presence)
        )
        conn.commit()
        conn.close()
        print(f"Registered student {full_name} with ID {sid}")

    def modify_student(self, sid, field, value):
        student = find_student(sid)
        if student and field in ALLOWED_STUDENT_FIELDS:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(f"UPDATE students SET {field} = ? WHERE id = ?", (value, sid))
            conn.commit()
            conn.close()
            print(f"Updated {field} for {student['full_name']} to {value}")
        else:
            print(f"Update failed")

    def remove_student(self, sid):
        student = find_student(sid)
        if student:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM students WHERE id = ?", (sid,))
            conn.commit()
            conn.close()
            print(f"Removed student {student['full_name']} with ID {sid}")
        else:
            print(f"Removal Failed")

    def register_teacher(self, tid, full_name, department, pay):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO teachers (id, full_name, department, pay) VALUES (?, ?, ?, ?)",
            (tid, full_name, department, pay)
        )
        conn.commit()
        conn.close()
        print(f"Registered teacher {full_name} with ID {tid}")

    def set_pay(self, tid, pay):
        teacher = find_teacher(tid)
        if teacher:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("UPDATE teachers SET pay = ? WHERE id = ?", (pay, tid))
            conn.commit()
            conn.close()
            print(f"Updated pay for {teacher['full_name']} to {pay}")
        else:
            print("Update failed")

    def remove_teacher(self, tid):
        teacher = find_teacher(tid)
        if teacher:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM teachers WHERE id = ?", (tid,))
            conn.commit()
            conn.close()
            print(f"Removed teacher {teacher['full_name']} with ID {tid}")
        else:
            print("Removal failed")