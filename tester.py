print("Hello")
print("Hi")

import csv

STUDENTS_FILE = "students.csv"
GRADES_FILE = "grades.csv"

students = {}
grades = []


def load_students():
    global students
    students = {}

    # Create the file if it doesn't exist, then read it
    file = open(STUDENTS_FILE, "a+")
    file.close()

    file = open(STUDENTS_FILE, "r")
    reader = csv.DictReader(file)

    for row in reader:
        if row["student_id"] and row["name"]:
            student_id = row["student_id"].strip()
            name = row["name"].strip()
            students[student_id] = name

    file.close()


def load_grades():
    global grades
    grades = []

    # Create the file if it doesn't exist, then read it
    file = open(GRADES_FILE, "a+")
    file.close()

    file = open(GRADES_FILE, "r")
    reader = csv.DictReader(file)

    for row in reader:
        if row["student_id"] and row["subject"] and row["mark"]:
            grade_entry = {
                "student_id": row["student_id"].strip(),
                "subject": row["subject"].strip(),
                "mark": float(row["mark"])
            }
            grades.append(grade_entry)

    file.close()


def save_students():
    file = open(STUDENTS_FILE, "w", newline="")
    fieldnames = ["student_id", "name"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for student_id in students:
        writer.writerow({
            "student_id": student_id,
            "name": students[student_id]
        })

    file.close()


def save_grades():
    file = open(GRADES_FILE, "w", newline="")
    fieldnames = ["student_id", "subject", "mark"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for grade_entry in grades:
        writer.writerow(grade_entry)

    file.close()