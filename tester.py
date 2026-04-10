import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, request, redirect, url_for
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

# Data structures
students = {}
grades = []

STUDENTS_FILE = "students.csv"
GRADES_FILE = "grades.csv"


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


def calculate_average(student_id):
    # Returns -1 if student has no grades
    total = 0
    count = 0

    for grade_entry in grades:
        if grade_entry["student_id"] == student_id:
            total = total + grade_entry["mark"]
            count = count + 1

    if count == 0:
        return -1

    average = total / count
    return average


def is_valid_mark(mark_input):
    # Checks the mark is a valid whole or decimal number
    if mark_input == "":
        return False

    dot_count = 0

    for character in mark_input:
        if character == ".":
            dot_count = dot_count + 1
            if dot_count > 1:
                return False
        elif character.isdigit() == False:
            return False

    return True


def fig_to_base64(fig):
    # Converts a matplotlib figure to a base64 string so it can be displayed in HTML
    img = io.BytesIO()
    FigureCanvas(fig).print_png(img)
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)
    return plot_url


def get_student_averages_chart():
    if len(students) == 0:
        return None

    student_names = []
    averages = []

    for student_id in students:
        name = students[student_id]
        average = calculate_average(student_id)

        if average != -1:
            student_names.append(name)
            averages.append(average)

    if len(student_names) == 0:
        return None

    fig = plt.figure(figsize=(10, 5))
    plt.bar(student_names, averages, color="skyblue")
    plt.xlabel("Student Name")
    plt.ylabel("Average Grade")
    plt.title("Student Average Grades")
    plt.ylim(0, 100)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    return fig_to_base64(fig)


def get_subject_averages_chart():
    if len(grades) == 0:
        return None

    subject_totals = {}
    subject_counts = {}

    for grade_entry in grades:
        subject = grade_entry["subject"]
        mark = grade_entry["mark"]

        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] = subject_totals[subject] + mark
        subject_counts[subject] = subject_counts[subject] + 1

    subject_names = []
    subject_averages = []

    for subject in subject_totals:
        average = subject_totals[subject] / subject_counts[subject]
        subject_names.append(subject)
        subject_averages.append(average)

    if len(subject_names) == 0:
        return None

    fig = plt.figure(figsize=(10, 5))
    plt.bar(subject_names, subject_averages, color="lightcoral")
    plt.xlabel("Subject")
    plt.ylabel("Average Grade")
    plt.title("Subject Average Grades")
    plt.ylim(0, 100)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    return fig_to_base64(fig)


def get_pass_fail_chart():
    if len(students) == 0:
        return None

    passing_count = 0
    failing_count = 0

    for student_id in students:
        average = calculate_average(student_id)

        if average == -1:
            continue

        if average >= 50:
            passing_count = passing_count + 1
        else:
            failing_count = failing_count + 1

    total = passing_count + failing_count

    if total == 0:
        return None

    labels = ["Passing (>= 50)", "Failing (< 50)"]
    sizes = [passing_count, failing_count]
    colors = ["lightgreen", "lightcoral"]

    fig = plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.title("Pass vs Fail Distribution")
    plt.tight_layout()

    return fig_to_base64(fig)


@app.route("/")
def index():
    load_students()
    load_grades()

    total_students = len(students)
    total_grades = len(grades)

    class_average = 0
    if total_students > 0:
        total_avg = 0
        count = 0
        for student_id in students:
            avg = calculate_average(student_id)
            if avg != -1:
                total_avg = total_avg + avg
                count = count + 1

        if count > 0:
            class_average = total_avg / count

    return render_template("index.html", total_students=total_students, total_grades=total_grades, class_average=round(class_average, 2))

@app.route("/students")
def view_students():
    load_students()
    load_grades()

    student_list = []

    for student_id in students:
        name = students[student_id]
        average = calculate_average(student_id)

        student_list.append({
            "student_id": student_id,
            "name": name,
            "average": average if average != -1 else None
        })

    return render_template("students.html", students=student_list)

@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        load_students()

        student_id = request.form.get("student_id").strip()
        name = request.form.get("name").strip()

        error = None

        if student_id == "":
            error = "Student ID cannot be empty."
        elif student_id in students:
            error = "Student ID already exists."
        elif name == "":
            error = "Name cannot be empty."

        if error:
            return render_template("add_student.html", error=error)

        students[student_id] = name
        save_students()

        return redirect(url_for("view_students"))

    return render_template("add_student.html")

@app.route("/delete-student/<student_id>", methods=["GET", "POST"])
def delete_student(student_id):
    load_students()
    load_grades()

    if student_id not in students:
        return redirect(url_for("view_students"))

    if request.method == "POST":
        name = students[student_id]
        del students[student_id]

        # Remove all grades belonging to this student
        i = 0
        while i < len(grades):
            if grades[i]["student_id"] == student_id:
                grades.pop(i)
            else:
                i = i + 1

        save_students()
        save_grades()

        return redirect(url_for("view_students"))

    name = students[student_id]
    return render_template("delete_student.html", student_id=student_id, name=name)

if __name__ == "__main__":
    load_students()
    load_grades()
    app.run(debug=True)