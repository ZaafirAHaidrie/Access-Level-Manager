from database import get_connection


def find_student(sid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (sid,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def find_teacher(tid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers WHERE id = ?", (tid,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def get_all_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_all_teachers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]