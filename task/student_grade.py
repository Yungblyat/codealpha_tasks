import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        letter_grade = self.calculate_letter_grade(grade)
        if subject in self.grades:
            self.grades[subject].append(letter_grade)
        else:
            self.grades[subject] = [letter_grade]

    def calculate_letter_grade(self, grade):
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_average(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)

        if all_grades:
            numerical_grades = [self.letter_to_numeric(grade) for grade in all_grades]
            average = sum(numerical_grades) / len(numerical_grades)
            return self.calculate_letter_grade(average)
        else:
            return None

    def letter_to_numeric(self, grade):
        if grade == 'A':
            return 90
        elif grade == 'B':
            return 80
        elif grade == 'C':
            return 70
        elif grade == 'D':
            return 60
        else:
            return 50

class StudentTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Grade Tracker")

        self.students = []

        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label_name = tk.Label(self.master, text="Student Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.label_subject = tk.Label(self.master, text="Subject:")
        self.label_subject.grid(row=1, column=0, padx=5, pady=5)
        self.label_grade = tk.Label(self.master, text="Grade:")
        self.label_grade.grid(row=2, column=0, padx=5, pady=5)

        # Entry fields
        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        self.entry_subject = tk.Entry(self.master)
        self.entry_subject.grid(row=1, column=1, padx=5, pady=5)
        self.entry_grade = tk.Entry(self.master)
        self.entry_grade.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.add_grade_button = tk.Button(self.master, text="Add Grade", command=self.add_grade)
        self.add_grade_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.calculate_average_button = tk.Button(self.master, text="Calculate Average", command=self.calculate_average)
        self.calculate_average_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Text area
        self.text_area = tk.Text(self.master, height=10, width=40)
        self.text_area.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_grade(self):
        name = self.entry_name.get()
        subject = self.entry_subject.get()
        grade_str = self.entry_grade.get()

        if not name:
            messagebox.showerror("Error", "Please enter student name.")
            return
        if not subject:
            messagebox.showerror("Error", "Please enter subject.")
            return
        if not grade_str:
            messagebox.showerror("Error", "Please enter grade.")
            return

        try:
            grade = float(grade_str)
        except ValueError:
            messagebox.showerror("Error", "Grade must be a number.")
            return

        if grade < 0 or grade > 100:
            messagebox.showerror("Error", "Grade must be between 0 and 100.")
            return

        student = None
        for s in self.students:
            if s.name == name:
                student = s
                break
        if not student:
            student = Student(name)
            self.students.append(student)

        student.add_grade(subject, grade)
        messagebox.showinfo("Success", "Grade added successfully.")

    def calculate_average(self):
        self.text_area.delete(1.0, tk.END)
        name = self.entry_name.get()

        if not name:
            messagebox.showerror("Error", "Please enter student name.")
            return

        for student in self.students:
            if student.name == name:
                average = student.calculate_average()
                if average is not None:
                    self.text_area.insert(tk.END, f"{student.name}'s overall average: {average}\n")
                else:
                    messagebox.showerror("Error", "No grades found for the student.")
                break
        else:
            messagebox.showerror("Error", "Student not found.")

def main():
    root = tk.Tk()
    app = StudentTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
