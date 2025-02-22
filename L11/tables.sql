DROP TABLE IF EXISTS 'student';
DROP TABLE IF EXISTS 'student_marks';
DROP TABLE IF EXISTS 'groups';
CREATE TABLE student (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE,
group_id INTEGER REFERENCES groups (id) NOT NULL);
INSERT INTO 'student' VALUES(1,'Максим',1);
INSERT INTO 'student' VALUES(2,'Антон',2);
INSERT INTO 'student' VALUES(3,'Михаил',3);
CREATE TABLE student_marks (
student_id INTEGER REFERENCES student (id) PRIMARY KEY,
math_mark_average FLOAT,
physics_mark_average FLOAT,
python_mark_average FLOAT);
INSERT INTO 'student_marks' VALUES(1,5,5,5);
INSERT INTO 'student_marks' VALUES(2,4,4.4,5);
INSERT INTO 'student_marks' VALUES(3,4.1,4.3,4.5);
CREATE TABLE groups (
id INTEGER PRIMARY KEY,
name VARCHAR(255) NOT NULL,
description VARCHAR(255));
INSERT INTO 'groups' VALUES(1,'БПИ2401','Первая группа');
INSERT INTO 'groups' VALUES(2,'БПИ2402','Вторая группа');
INSERT INTO 'groups' VALUES(3,'БПИ2403','Третья группа');
