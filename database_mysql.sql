CREATE DATABASE timetable_db;
USE timetable_db;
SHOW DATABASES;
USE timetable_db;
drop table timetable;
CREATE TABLE faculty(
faculty_id int primary key,
faculty_name varchar(100),
department varchar(100)
);
CREATE TABLE subjects(
subject_id int primary key,
subject_name varchar(100),
id int,
foreign key(id) references faculty(id)
);
CREATE TABLE rooms(
room_id int primary key,
room_name varchar(100),
capacity int
);
CREATE TABLE classes(
class_id int primary key,
class_name varchar(100),
students int
);
CREATE TABLE timeslots(
timeslot_id int primary key,
day varchar(50),
slot_time varchar(50)
);
CREATE TABLE timetable(
timetable_id int primary key,
class_id int,
subject_id int,
faculty_id int,
room_id int,
timeslot_id int,
foreign key(class_id) references classes(class_id),
foreign key(subject_id) references subjects(subject_id),
foreign key(id) references faculty(id),
foreign key(room_id) references rooms(room_id),
foreign key(timeslot_id) references timeslots(timeslot_id)
);
insert into faculty (id, name, department) values
(001,'Dr. Sharma','MCA'),
(002,'Dr. Mehta','MCA'),
(003,'Dr. Kaur','BCA');
insert into rooms (room_id, room_name, capacity) values
(101,'B7101',50),
(102,'B7102',60),
(103,'B7103',40);
insert into classes (class_id, class_name, students) values
(01,'MCA-2',55),
(02,'MCA-4',50),
(03,'BCA-2AB',60);
insert into subjects (subject_id, subject_name, id) values
(1,'ML',001),
(2,'CC',002),
(3,'AWT',003);
insert into timeslots (timeslot_id, day, slot_time) values
(11,'Monday','9-10'),
(12,'Monday','10-11'),
(13,'Tuesday','11-12'),
(14,'Tuesday','10-11');

use timetable_db;
SELECT * FROM classes;
ALTER TABLE subjects CHANGE id faculty_id int;
describe subjects;
SELECT * FROM faculty;
ALTER TABLE timetable CHANGE id faculty_id int ;
use timetable_db;
ALTER TABLE subjects CHANGE id faculty_id int;
use timetable_db;
ALTER TABLE subjects CHANGE id faculty_id int;
select * from faculty;
use timetable_db;
describe subjects;
ALTER TABLE subjects CHANGE id faculty_id int;
select database();
use timetable_db;
select database();
use timetable_db;
describe timetable;

drop table if exists timetable;
drop table if exists subjects;
drop table if exists classes;
drop table if exists rooms;
drop table if exists faculty;
drop table if exists timeslots;
CREATE TABLE faculty(
    faculty_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

CREATE TABLE classes(
    class_id INT PRIMARY KEY,
    class_name VARCHAR(50),
    students INT
);

CREATE TABLE rooms(
    room_id INT PRIMARY KEY,
    room_name VARCHAR(50),
    capacity INT
);

CREATE TABLE subjects(
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(50),
    faculty_id INT,
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

CREATE TABLE timeslots(
    timeslot_id INT PRIMARY KEY,
    day VARCHAR(20),
    slot_time VARCHAR(20)
);

CREATE TABLE timetable(
    timetable_id INT AUTO_INCREMENT PRIMARY KEY,
    class_id INT,
    subject_id INT,
    faculty_id INT,
    room_id INT,
    timeslot_id INT,
    FOREIGN KEY (class_id) REFERENCES classes(class_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    FOREIGN KEY (timeslot_id) REFERENCES timeslots(timeslot_id)
);
INSERT INTO faculty VALUES
(1,'Dr. Sharma','MCA'),
(2,'Dr. Mehta','MCA'),
(3,'Dr. Kaur','BCA');

INSERT INTO classes VALUES
(1,'MCA-2',55),
(2,'MCA-4',50),
(3,'BCA-2A',60);

INSERT INTO rooms VALUES
(101,'B101',50),
(102,'B102',60),
(103,'B103',40);

INSERT INTO subjects VALUES
(1,'ML',1),
(2,'CC',2),
(3,'AWT',3);

INSERT INTO timeslots VALUES
(1,'Monday','9-10'),
(2,'Monday','10-11'),
(3,'Tuesday','11-12'),
(4,'Tuesday','10-11');
describe faculty;
describe timetable;
