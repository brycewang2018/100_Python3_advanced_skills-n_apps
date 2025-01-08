#pip install tkinter -q
import tkinter as tk
from tkinter import messagebox
import os

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
    return [tuple(line.strip().split(",")) for line in lines if line.strip()]

def write_data(name, english, math, physics, ml):
    """Write a new record to the data file."""
    with open(data_file, "a") as f:
        f.write(f"{name},{english},{math},{physics},{ml}\n")

def add_student():
    name = name_entry.get().strip()
    english = english_entry.get().strip()
    math = math_entry.get().strip()
    physics = physics_entry.get().strip()
    ml = ml_entry.get().strip()

    if not name or not english or not math or not physics or not ml:
        messagebox.showerror("Error", "All fields are required!")
        return

    write_data(name, english, math, physics, ml)
    messagebox.showinfo("Success", "Student added successfully!")
    name_entry.delete(0, tk.END)
    english_entry.delete(0, tk.END)
    math_entry.delete(0, tk.END)
    physics_entry.delete(0, tk.END)
    ml_entry.delete(0, tk.END)
    display_students()

def display_students():
    """Display all student records in the table."""
    students = read_data()
    for widget in student_table_frame.winfo_children():
        widget.destroy()

    headers = ["Name", "English", "Math", "Physics", "Machine Learning"]
    for col, header in enumerate(headers):
        tk.Label(student_table_frame, text=header, borderwidth=1, relief="solid", width=15).grid(row=0, column=col)

    for row, student in enumerate(students, start=1):
        for col, value in enumerate(student):
            tk.Label(student_table_frame, text=value, borderwidth=1, relief="solid", width=15).grid(row=row, column=col)

# Create the main window
root = tk.Tk()
root.title("Student Grade Management")

# Input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="English:").grid(row=1, column=0, padx=5, pady=5)
english_entry = tk.Entry(input_frame)
english_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Math:").grid(row=2, column=0, padx=5, pady=5)
math_entry = tk.Entry(input_frame)
math_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Physics:").grid(row=3, column=0, padx=5, pady=5)
physics_entry = tk.Entry(input_frame)
physics_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Machine Learning:").grid(row=4, column=0, padx=5, pady=5)
ml_entry = tk.Entry(input_frame)
ml_entry.grid(row=4, column=1, padx=5, pady=5)

# Add student button
tk.Button(input_frame, text="Add Student", command=add_student).grid(row=5, columnspan=2, pady=10)

# Student table
student_table_frame = tk.Frame(root)
student_table_frame.pack(pady=10)

display_students()

# Run the application
root.mainloop()