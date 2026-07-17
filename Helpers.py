from records import student_records, teacher_records


def find_student(sid):
    for student in student_records:
        if student["id"] == sid:
            return student
    return None


def find_teacher(tid):
    for teacher in teacher_records:
        if teacher["id"] == tid:
            return teacher
    return None