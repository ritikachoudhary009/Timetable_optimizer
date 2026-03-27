# Timetable_optimizer
# 📅 Timetable Management System (Flask)

A  **Timetable Optimizer** built  using **Flask** and **MySQL** that allows administrators to manage faculty, classes, subjects, rooms, and generate timetables efficiently.

---

## 🚀 Features

* 👨‍🏫 Manage Faculty (Add, Update, Delete)
* 🏫 Manage Classes & Departments
* 📚 Manage Subjects
* 🏢 Manage Rooms
* ⏰ Manage Time Slots
* 🔄 Allocate Faculty, Room, Subject & Class
* ⚠️ Clash Detection System (Prevents scheduling conflicts)
* 📊 Dashboard Overview
* 📅 Generate Timetable View

---

## 🧠 Technologies Used

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, Jinja2 Templates
* **Database:** MySQL
* **Architecture:** MVC (Model-View-Controller)

---

## ⚙️ Installation


### Install Dependencies

```bash
pip install flask mysql-connector-python
```

###  Setup Database

* Create a MySQL database
* Create tables:

  * faculty
  * rooms
  * subjects
  * classes
  * timeslots
  * allocation

(Update your `database.py` with credentials)

---

## ▶️ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---



## 🧩 Project Structure

```
project/
│── app.py
│── database.py
│── optimizer.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── faculty.html
│   ├── classes.html
│   ├── rooms.html
│   ├── subjects.html
│   ├── timeslots.html
│   ├── allocation.html
│   └── timetable.html
│
├── static/
│   ├── css/
│   └── js/
```

---

## ⚠️ Constraints Implemented

* ❌ No faculty can be assigned to multiple classes at the same time
* ❌ No room can be used for multiple classes simultaneously
* ❌ No class can have multiple subjects in the same time slot
* ❌ Duplicate time slots are not allowed
* 🍱 Fixed lunch break (1:00 PM – 2:00 PM)

---

## 🧮 Algorithms Used

* Constraint Checking (Clash Detection)
* CRUD Operations
* Data Mapping for Timetable Generation

---

## 🚧 Future Improvements

* 🤖 Automatic timetable generation (Genetic Algorithm)
* 📊 Faculty availability preferences
* 🏫 Room capacity validation
* 📈 Smart optimization of schedules

---

