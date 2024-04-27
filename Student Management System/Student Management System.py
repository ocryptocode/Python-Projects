import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import bs4
import matplotlib.pyplot as plt
import sqlite3

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600+400+100")
        self.root.title("Student Management System")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.location_label = tk.Label(self.root, text="Location:")
        self.location_label.grid(row=0, column=0, sticky="w")
        self.location_value = tk.Label(self.root, text=self.get_location())
        self.location_value.grid(row=0, column=1, sticky="w")

        self.temperature_label = tk.Label(self.root, text="Temperature:")
        self.temperature_label.grid(row=1, column=0, sticky="w")
        self.temperature_value = tk.Label(self.root, text=self.get_temperature())
        self.temperature_value.grid(row=1, column=1, sticky="w")

        self.qotd_label = tk.Label(self.root, text="Quote of the Day:")
        self.qotd_label.grid(row=2, column=0, sticky="w")
        self.qotd_value = tk.Message(self.root, text=self.get_qotd(), width=400)
        self.qotd_value.grid(row=2, column=1, sticky="w")

        self.btn_add = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.btn_add.grid(row=3, column=0, pady=10)

        self.btn_view = tk.Button(self.root, text="View Students", command=self.view_students)
        self.btn_view.grid(row=3, column=1, pady=10)

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def get_location(self):
        # Use IP Geolocation API to get location
        return "New York, USA"  # Example location

    def get_temperature(self):
        # Use Weather API to get temperature
        return "25°C"  # Example temperature

    def get_qotd(self):
        # Scrape Quote of the Day from a website
        return "This is the Quote of the Day"  # Example quote

    def add_student(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Student")

        # Add student entry fields
        tk.Label(add_window, text="Roll No:").grid(row=0, column=0)
        roll_entry = tk.Entry(add_window)
        roll_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Marks:").grid(row=2, column=0)
        marks_entry = tk.Entry(add_window)
        marks_entry.grid(row=2, column=1)

        def save_student():
            roll = roll_entry.get()
            name = name_entry.get()
            marks = marks_entry.get()
            # Add student to database
            messagebox.showinfo("Success", "Student added successfully")
            add_window.destroy()

        tk.Button(add_window, text="Save", command=save_student).grid(row=3, columnspan=2, pady=10)

    def view_students(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Students")

        text_area = scrolledtext.ScrolledText(view_window, width=40, height=10)
        text_area.grid(row=0, column=0, padx=10, pady=10)

        # Fetch and display students from database
        text_area.insert(tk.END, "List of Students\n")

        # Example data
        students = [("1", "John", "85"), ("2", "Alice", "90"), ("3", "Bob", "75")]

        for student in students:
            text_area.insert(tk.END, f"Roll No: {student[0]}, Name: {student[1]}, Marks: {student[2]}\n")

def main():
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
