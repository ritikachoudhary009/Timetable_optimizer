from database import get_connection

# Classes Model
def get_classes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes")
    return cursor.fetchall()


# Faculty Model
def get_faculty():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM faculty")
    return cursor.fetchall()


# Rooms Model
def get_rooms():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms")
    return cursor.fetchall()


# Subjects Model
def get_subjects():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    return cursor.fetchall()


# Timeslots Model
def get_timeslots():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM timeslots")
    return cursor.fetchall()


# Timetable Model
def get_timetable():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM timetable")
    return cursor.fetchall()