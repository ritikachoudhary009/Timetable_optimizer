
from flask import Flask, render_template, render_template_string, jsonify, flash
from database import get_connection
from flask import request, redirect
from optimizer import generate_timetable


app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = "timetable_secret"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM faculty")
    faculty_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM rooms")
    room_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM subjects")
    subject_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM classes")
    class_count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return render_template(
        "dashboard.html",
        faculty_count=faculty_count,
        room_count=room_count,
        subject_count=subject_count,
        class_count=class_count
    )


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":
        return redirect("/dashboard")
    else:
        return "Invalid Credentials"

#get classes   
@app.route("/add-class", methods=["POST"])
def add_class():
    class_name = request.form["class_name"]
    department= request.form["department"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO classes (class_name, department) VALUES (%s, %s)",
        (class_name, department)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/classes-page")
@app.route("/classes-page")
def classes_page():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM classes")
    classes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("classes.html", classes=classes)

#delete class
@app.route("/delete-class/<int:id>")
def delete_class(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM classes WHERE class_id=%s", (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/classes-page")

#edit faculty
@app.route("/update-class/<int:id>", methods=["POST"])
def update_class(id):
    class_name = request.form["class_name"]
    department = request.form["department"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE classes SET class_name=%s, department=%s WHERE class_id=%s",
        (class_name, department, id)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/classes-page")


# Get Faculty
@app.route("/add-faculty", methods=["POST"])
def add_faculty():
    faculty_name = request.form["faculty_name"]
    subject = request.form["subject"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO faculty (name, subject) VALUES (%s, %s)",
        (faculty_name, subject)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/faculty-page")
@app.route("/faculty-page")
def faculty_page():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faculty")
    faculty = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("faculty.html", faculty=faculty)

#delete button
@app.route("/delete-faculty/<int:id>")
def delete_faculty(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM faculty WHERE faculty_id=%s", (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/faculty-page")

#edit faculty
@app.route("/update-faculty/<int:id>", methods=["POST"])
def update_faculty(id):
    faculty_name = request.form["faculty_name"]
    subject = request.form["subject"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE faculty SET name=%s, subject=%s WHERE faculty_id=%s",
        (faculty_name, subject, id)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/faculty-page")



# Get Rooms
@app.route("/add-room", methods=["POST"])
def add_room():
    room_number = request.form["room_number"]
    capacity = request.form["capacity"]
    class_type = request.form["class_type"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO rooms (room_number, capacity, class_type) VALUES (%s, %s, %s)",
        (room_number, capacity, class_type)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/rooms-page")

@app.route("/rooms-page")
def rooms_page():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("rooms.html", rooms=rooms)

@app.route("/delete-room/<room_number>")
def delete_room(room_number):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM rooms WHERE room_number=%s", (room_number,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/rooms-page")

@app.route("/update-room/<room_number>", methods=["POST"])
def update_room(room_number):
    new_room_number = request.form["room_number"]
    capacity = request.form["capacity"]
    class_type = request.form["class_type"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE rooms SET room_number=%s, capacity=%s, class_type=%s WHERE room_number=%s",
        (new_room_number, capacity, class_type, room_number)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/rooms-page")


# Get Subjects

@app.route("/add-subject", methods=["POST"])
def add_subject():
    subject_name = request.form["subject_name"]
    subject_code = request.form["subject_code"]
    hours_per_week = request.form["hours_per_week"]
    class_type = request.form["class_type"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO subjects (subject_name, subject_code, hours_per_week, class_type) VALUES (%s, %s, %s, %s)",
        (subject_name, subject_code, hours_per_week, class_type)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/subjects-page")
@app.route("/subjects-page")
def subjects_page():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("subjects.html", subjects=subjects)

@app.route("/delete-subject/<int:id>")
def delete_subject(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM subjects WHERE subject_id=%s", (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/subjects-page")

@app.route("/update-subject/<subject_name>", methods=["POST"])
def update_subject(subject_name):
    new_subject_name = request.form["subject_name"]
    subject_code = request.form["subject_code"]
    hours_per_week = request.form["hours_per_week"]
    class_type = request.form["class_type"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE subjects SET subject_name=%s, subject_code=%s, hours_per_week=%s, class_type=%s WHERE subject_name=%s",
        (new_subject_name, subject_code, hours_per_week, class_type, subject_name)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/subjects-page")

# Get Timeslots
@app.route('/add-timeslot', methods=['POST'])
def add_timeslot():
    start_time = request.form['start_time']
    end_time = request.form['end_time']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM timeslots
        WHERE start_time=%s AND end_time=%s
    """, (start_time, end_time))

    existing = cursor.fetchone()

    if existing:
        return "Timeslot already exists"

    cursor.execute("""
        INSERT INTO timeslots(start_time, end_time)
        VALUES (%s,%s)
    """, (start_time, end_time))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/timeslots-page')
@app.route("/timeslots-page")
def timeslot_page():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM timeslots")
    timeslots = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("timeslots.html", timeslots=timeslots)


#Allocation_table
@app.route('/allocation-page')
def allocation_page():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faculty")
    faculty = cursor.fetchall()

    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()

    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()

    cursor.execute("SELECT * FROM timeslots")
    timeslots = cursor.fetchall()

    cursor.execute("SELECT * FROM classes")
    classes = cursor.fetchall()

    cursor.execute("""
        SELECT allocation.allocation_id,
               faculty.name,
               subjects.subject_name,
               rooms.room_number,
               timeslots.start_time,
               timeslots.end_time,
               classes.class_name,
               allocation.day
        FROM allocation
        JOIN faculty ON allocation.faculty_id = faculty.faculty_id
        JOIN subjects ON allocation.subject_id = subjects.subject_id
        JOIN rooms ON allocation.room_id = rooms.room_id
        JOIN timeslots ON allocation.timeslot_id = timeslots.timeslot_id
        JOIN classes ON allocation.class_id = classes.class_id
                   
        ORDER BY allocation.allocation_id ASC
    """)

    allocations = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'allocation.html',
        faculty=faculty,
        subjects=subjects,
        rooms=rooms,
        timeslots=timeslots,
        classes=classes,
        allocations=allocations
    )

@app.route('/add-allocation', methods=['POST'])
def add_allocation():
    faculty_id = int(request.form['faculty_id'])
    subject_id = int(request.form['subject_id'])
    room_id = int(request.form['room_id'])
    class_id = int(request.form['class_id'])
    timeslot_id = int(request.form['timeslot_id'])
    day = request.form['day']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT allocation_id FROM allocation
        WHERE day=%s
        AND timeslot_id=%s
        AND (
            faculty_id=%s
            OR room_id=%s
            OR class_id=%s
        )
    """, (day, timeslot_id, faculty_id, room_id, class_id))

    clash = cursor.fetchone()

    if clash:
        flash("Clash detected! Faculty / Room / Class already assigned.", "danger")
        cursor.close()
        conn.close()
        return redirect('/allocation-page')

    cursor.execute("""
        INSERT INTO allocation
        (faculty_id, subject_id, room_id, timeslot_id, class_id, day)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (faculty_id, subject_id, room_id, timeslot_id, class_id, day))

    conn.commit()

    flash("Allocation added successfully!", "success")

    cursor.close()
    conn.close()

    return redirect('/allocation-page')

#Timetable_page
@app.route('/timetable-page')
def timetable_page():

    timetable = {
        "9:00 - 10:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "10:00 - 11:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "11:00 - 12:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "12:00 - 1:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "1:00 - 2:00": {"Mon": "Lunch Break", "Tue": "Lunch Break", "Wed": "Lunch Break", "Thu": "Lunch Break", "Fri": "Lunch Break"},
        "2:00 - 3:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "3:00 - 4:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""}
    }

    return render_template('timetable.html', timetable=timetable)


# Get Generated Timetable
@app.route('/generate-timetable', methods=['GET'])
def generate_timetable_page():
    conn = get_connection()
    cursor = conn.cursor()

    # Fixed weekly structure
    timetable = {
        "9:00:00 - 10:00:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "10:00:00 - 11:00:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "11:00:00 - 12:00:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "12:00:00 - 1:00:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "1:00:00 - 2:00:00": {
            "Mon": "Lunch Break",
            "Tue": "Lunch Break",
            "Wed": "Lunch Break",
            "Thu": "Lunch Break",
            "Fri": "Lunch Break"
        },
        "2:00:00 - 3:00:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""},
        "3:00:00 - 4:00:00": {"Mon": "", "Tue": "", "Wed": "", "Thu": "", "Fri": ""}
    }

    cursor.execute("""
        SELECT 
            allocation.day,
            timeslots.start_time,
            timeslots.end_time,
            subjects.subject_name,
            faculty.name,
            rooms.room_number,
            classes.class_name
        FROM allocation
        JOIN timeslots ON allocation.timeslot_id = timeslots.timeslot_id
        JOIN subjects ON allocation.subject_id = subjects.subject_id
        JOIN faculty ON allocation.faculty_id = faculty.faculty_id
        JOIN rooms ON allocation.room_id = rooms.room_id
        JOIN classes ON allocation.class_id = classes.class_id
    """)

    rows = cursor.fetchall()

    day_map = {
        "Monday": "Mon",
        "Tuesday": "Tue",
        "Wednesday": "Wed",
        "Thursday": "Thu",
        "Friday": "Fri"
    }

    for row in rows:
        day = day_map[row[0]]

        time = f"{row[1]} - {row[2]}"

        cell = f"{row[3]}<br>{row[4]}<br>{row[5]}<br>{row[6]}"

        if time in timetable:
            timetable[time][day] = cell

    cursor.close()
    conn.close()

    return render_template("timetable.html", timetable=timetable)


#delete allocation
@app.route('/delete-allocation/<int:id>')
def delete_allocation(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM allocation WHERE allocation_id=%s", (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/allocation-page')


#edit allocation
@app.route('/update-allocation', methods=['POST'])
def update_allocation():
    allocation_id = request.form['allocation_id']
    faculty_id = request.form['faculty_id']
    subject_id = request.form['subject_id']
    room_id = request.form['room_id']
    class_id = request.form['class_id']
    timeslot_id = request.form['timeslot_id']
    day = request.form['day']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE allocation
        SET faculty_id=%s, subject_id=%s, room_id=%s,
            class_id=%s, timeslot_id=%s, day=%s
        WHERE allocation_id=%s
    """, (faculty_id, subject_id, room_id, class_id, timeslot_id, day, allocation_id))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/allocation-page')

if __name__ == "__main__":
    app.run(debug=True)