#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
# student_grades.py
import cgi
import os
print("Content-Type: text/html\n")

data_file = "students_data.txt"

# Ensure the data file exists
if not os.path.exists(data_file):
    open(data_file, 'w').close()

def read_data():
    """Read data from the file and return it as a list of tuples."""
    if not os.path.exists(data_file):
        return []
    with open(data_file, "r") as f:
        lines = f.readlines()
    if not lines:  # 如果文件为空
        print("<p>No students found. Add some students!</p>")
    return [tuple(line.strip().split(",")) for line in lines if line.strip()]


def write_data(name, grade):
    """Write a new record to the data file."""
    with open(data_file, "a") as f:
        f.write(f"{name},{grade}\n")

def display_students():
    """Display all student records."""
    students = read_data()
    html = "<table border='1'><tr><th>Name</th><th>Grade</th></tr>"
    for name, grade in students:
        html += f"<tr><td>{name}</td><td>{grade}</td></tr>"
    html += "</table>"
    return html

print("Content-Type: text/html\n")
print("""
<html>
<head>
    <title>Student Grade Management</title>
</head>
<body>
<h1>Student Grade Management</h1>
<form method="post" action="student_grades.py">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br>
    <label for="grade">Grade:</label>
    <input type="text" id="grade" name="grade" required><br>
    <input type="submit" value="Add Student">
</form>
""")

form = cgi.FieldStorage()
name = form.getvalue("name")
grade = form.getvalue("grade")

if name and grade:
    write_data(name, grade)
    print("<p>Student added successfully!</p>")

print("<h2>Student List</h2>")
print(display_students())

print("""
</body>
</html>
""")