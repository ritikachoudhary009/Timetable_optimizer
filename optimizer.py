import random
from database import get_connection
from models import get_classes, get_subjects, get_rooms, get_timeslots

def generate_timetable():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM timetable")
    conn.commit()

    classes = get_classes()
    subjects = get_subjects()
    rooms = get_rooms()
    timeslots = get_timeslots()

    timetable_data = []

    for c in classes:
        class_id = c[0]

        for s in subjects:
            subject_id = s[0]
            faculty_id = s[2]   # faculty linked to subject

            room = random.choice(rooms)
            slot = random.choice(timeslots)

            timetable_data.append(
                (class_id, subject_id, faculty_id, room[0], slot[0])
            )

    for entry in timetable_data:

        cursor.execute("""
        INSERT INTO timetable(class_id,subject_id,faculty_id,room_id,timeslot_id)
        VALUES (%s,%s,%s,%s,%s)
        """, entry)

    conn.commit()
    cursor.close()
    conn.close()

    return "Timetable Generated"