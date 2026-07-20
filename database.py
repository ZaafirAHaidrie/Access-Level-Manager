import sqlite3

DB_NAME = "school.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            grade TEXT,
            score INTEGER DEFAULT 0,
            presence INTEGER DEFAULT 0
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            department TEXT,
            pay INTEGER
        )
    """)
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM students")
    if cur.fetchone()[0] == 0:
        seed_students = [
            (1, "Sakeena Batool", "11-A", 95, 98),
            (2, "Abdul Samad", "11-B", 88, 92),
            (3, "Faaiz Khan", "11-C", 76, 85),
            (4, "Ahmed Raza", "11-A", 92, 97),
            (5, "Juwairiah Awais", "11-B", 84, 90),
            (6, "Haider Ali", "11-C", 79, 88),
            (7, "Azaan Zakir", "11-A", 91, 95),
            (8, "Ahsan Ali", "11-B", 87, 93),
            (9, "Muhammad Musab", "11-C", 82, 89),
            (10, "Zaafir Haidrie", "11-A", 98, 96),
            (11, "Zara Khan", "11-B", 85, 91),
            (12, "Malaika Subhani", "11-C", 78, 87),
            (13, "Hamza Saqib", "11-A", 93, 94),
            (14, "Murtaza Ali", "11-B", 89, 90),
            (15, "Abdullah Ehsan", "11-C", 81, 86),
        ]
        cur.executemany(
            "INSERT INTO students (id, full_name, grade, score, presence) VALUES (?, ?, ?, ?, ?)",
            seed_students
        )

    cur.execute("SELECT COUNT(*) FROM teachers")
    if cur.fetchone()[0] == 0:
        seed_teachers = [
            (206, "Mr. Ahmed Maqsood", "Mathematics", 50000),
            (192, "Mr. Rao Habib", "English", 48000),
            (453, "Mr. Usama Virk ", "Computer Science", 52000),
            (723, "Mr. Bari", "History & Geography", 63000),
            (105, "Mr. Hamiz Javed", "Physics", 49000),
            (309, "Mr. Hashim Ali", "Chemistry", 51000),
            (412, "Mr. Taimoor Shakoori", "Biology", 47000),
        ]
        cur.executemany(
            "INSERT INTO teachers (id, full_name, department, pay) VALUES (?, ?, ?, ?)",
            seed_teachers
        )

    conn.commit()
    conn.close()