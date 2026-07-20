from database import create_connection

def studentsearch(student_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    connection.close()
    return dict(student) if student else None

def teachersearch(teacher_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM teachers WHERE id = ?", (teacher_id,))
    teacher = cursor.fetchone()
    connection.close()
    return dict(teacher) if teacher else None

def view_all_students():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    connection.close()
    return [dict(student) for student in students]

def view_all_teachers():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM teachers")
    teachers = cursor.fetchall()
    connection.close()
    return [dict(teacher) for teacher in teachers]
