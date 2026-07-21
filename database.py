import sqlite3
DB_NAME = 'schoolrecord.db'

def create_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection
def initialize_database():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    full_name TEXT NOT NULL,
                    grade TEXT,
                    score INTEGER DEFAULT 0,
                    presence INTEGER DEFAULT 0
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    full_name TEXT NOT NULL,
                    department TEXT,
                    pay INTEGER
        )
    """)
    connection.commit()
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        enter_students = [
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

        cursor.executemany(
            "INSERT INTO students (id, full_name, grade, score, presence) VALUES (?, ?, ?, ?, ?)",
            enter_students
        )
    cursor.execute("SELECT COUNT(*) FROM teachers")
    if cursor.fetchone()[0] == 0:
        enter_teachers = [
            (2060, "Mr. Ahmed Maqsood", "Mathematics", 50000),
            (1920, "Mr. Rao Habib", "English", 48000),
            (4530, "Mr. Usama Virk ", "Computer Science", 52000),
            (7230, "Mr. Bari", "History & Geography", 63000),
            (1050, "Mr. Hamiz Javed", "Physics", 49000),
            (3090, "Mr. Hashim Ali", "Chemistry", 51000),
            (4120, "Mr. Taimoor Shakoori", "Biology", 47000),
        ]
        cursor.executemany(
            "INSERT INTO teachers (id, full_name, department, pay) VALUES (?, ?, ?, ?)",
            enter_teachers
        )
    connection.commit()
    connection.close()
    
        