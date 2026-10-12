import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt


# =========================
# ACADEMIC PERFORMANCE TRACKER
# =========================

SUBJECTS = ["Python", "Java", "Mathematics", "DBMS", "English"]


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def grade_point(grade):
    points = {
        "A+": 10,
        "A": 9,
        "B": 8,
        "C": 7,
        "D": 6,
        "F": 0
    }
    return points[grade]


def subject_performance(mark):
    if mark >= 80:
        return "Strong"
    elif mark < 50:
        return "Weak"
    else:
        return "Average"


def calculate_cgpa(previous_gpas, current_gpa):
    if previous_gpas:
        all_gpas = previous_gpas + [current_gpa]
        return sum(all_gpas) / len(all_gpas)
    return current_gpa


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("Academic Performance Tracker")
root.geometry("1050x760")
root.minsize(950, 700)
root.configure(bg="#F4F7FB")


# =========================
# STYLE
# =========================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TEntry",
    padding=7,
    font=("Segoe UI", 10)
)

style.configure(
    "TButton",
    font=("Segoe UI", 10, "bold"),
    padding=9
)

style.configure(
    "Treeview",
    font=("Segoe UI", 10),
    rowheight=32,
    background="white",
    fieldbackground="white"
)

style.configure(
    "Treeview.Heading",
    font=("Segoe UI", 10, "bold"),
    padding=8
)


# =========================
# HEADER
# =========================

header = tk.Frame(root, bg="#17324D", height=95)
header.pack(fill="x")
header.pack_propagate(False)

title = tk.Label(
    header,
    text="ACADEMIC PERFORMANCE TRACKER",
    font=("Segoe UI", 22, "bold"),
    bg="#17324D",
    fg="white"
)
title.pack(pady=(18, 2))

subtitle = tk.Label(
    header,
    text="Student Performance & Analytics System",
    font=("Segoe UI", 10),
    bg="#17324D",
    fg="#D9E8F5"
)
subtitle.pack()


# =========================
# MAIN CONTAINER
# =========================

main = tk.Frame(root, bg="#F4F7FB")
main.pack(fill="both", expand=True, padx=22, pady=18)


# =========================
# STUDENT INFORMATION
# =========================

student_card = tk.LabelFrame(
    main,
    text="  STUDENT INFORMATION  ",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="#17324D",
    padx=15,
    pady=12
)
student_card.pack(fill="x", pady=(0, 14))


tk.Label(
    student_card,
    text="Student Name",
    font=("Segoe UI", 10, "bold"),
    bg="white"
).grid(row=0, column=0, sticky="w", padx=8, pady=6)

name_entry = ttk.Entry(student_card, width=28)
name_entry.grid(row=0, column=1, padx=8, pady=6)

tk.Label(
    student_card,
    text="Roll Number",
    font=("Segoe UI", 10, "bold"),
    bg="white"
).grid(row=0, column=2, sticky="w", padx=8, pady=6)

roll_entry = ttk.Entry(student_card, width=20)
roll_entry.grid(row=0, column=3, padx=8, pady=6)

tk.Label(
    student_card,
    text="Semester",
    font=("Segoe UI", 10, "bold"),
    bg="white"
).grid(row=0, column=4, sticky="w", padx=8, pady=6)

semester_entry = ttk.Entry(student_card, width=15)
semester_entry.grid(row=0, column=5, padx=8, pady=6)


# =========================
# INPUT AREA
# =========================

input_frame = tk.Frame(main, bg="#F4F7FB")
input_frame.pack(fill="x", pady=(0, 14))


# =========================
# SUBJECT MARKS
# =========================

marks_card = tk.LabelFrame(
    input_frame,
    text="  SUBJECT MARKS  ",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="#17324D",
    padx=15,
    pady=12
)
marks_card.pack(side="left", fill="both", expand=True, padx=(0, 8))


mark_entries = {}

for i, subject in enumerate(SUBJECTS):
    tk.Label(
        marks_card,
        text=subject,
        font=("Segoe UI", 10),
        bg="white"
    ).grid(row=i, column=0, sticky="w", padx=8, pady=5)

    entry = ttk.Entry(marks_card, width=15)
    entry.grid(row=i, column=1, padx=8, pady=5)

    mark_entries[subject] = entry


# =========================
# ATTENDANCE
# =========================

attendance_card = tk.LabelFrame(
    input_frame,
    text="  ATTENDANCE & GPA  ",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="#17324D",
    padx=15,
    pady=12
)
attendance_card.pack(side="right", fill="both", expand=True, padx=(8, 0))


tk.Label(
    attendance_card,
    text="Total Classes",
    font=("Segoe UI", 10),
    bg="white"
).grid(row=0, column=0, sticky="w", padx=8, pady=8)

total_entry = ttk.Entry(attendance_card, width=20)
total_entry.grid(row=0, column=1, padx=8, pady=8)


tk.Label(
    attendance_card,
    text="Classes Attended",
    font=("Segoe UI", 10),
    bg="white"
).grid(row=1, column=0, sticky="w", padx=8, pady=8)

attended_entry = ttk.Entry(attendance_card, width=20)
attended_entry.grid(row=1, column=1, padx=8, pady=8)


tk.Label(
    attendance_card,
    text="Previous GPAs",
    font=("Segoe UI", 10),
    bg="white"
).grid(row=2, column=0, sticky="w", padx=8, pady=8)

previous_gpa_entry = ttk.Entry(attendance_card, width=20)
previous_gpa_entry.grid(row=2, column=1, padx=8, pady=8)

tk.Label(
    attendance_card,
    text="Example: 8.2, 8.7",
    font=("Segoe UI", 8),
    fg="#777777",
    bg="white"
).grid(row=3, column=1, sticky="w", padx=8)


# =========================
# SUMMARY CARDS
# =========================

summary_frame = tk.Frame(main, bg="#F4F7FB")
summary_frame.pack(fill="x", pady=(0, 14))

summary_data = [
    ("Percentage", "--"),
    ("Grade", "--"),
    ("GPA", "--"),
    ("CGPA", "--"),
    ("Attendance", "--")
]

summary_labels = {}

for i, (title_text, value) in enumerate(summary_data):

    card = tk.Frame(
        summary_frame,
        bg="white",
        bd=1,
        relief="solid"
    )

    card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=5
    )

    tk.Label(
        card,
        text=title_text,
        font=("Segoe UI", 9, "bold"),
        bg="white",
        fg="#666666"
    ).pack(pady=(10, 2))

    value_label = tk.Label(
        card,
        text=value,
        font=("Segoe UI", 17, "bold"),
        bg="white",
        fg="#17324D"
    )

    value_label.pack(pady=(0, 10))

    summary_labels[title_text] = value_label


# =========================
# BUTTONS
# =========================

button_frame = tk.Frame(main, bg="#F4F7FB")
button_frame.pack(fill="x", pady=(0, 14))


# =========================
# REPORT TABLE
# =========================

report_card = tk.LabelFrame(
    main,
    text="  SUBJECT PERFORMANCE ANALYSIS  ",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="#17324D",
    padx=10,
    pady=10
)
report_card.pack(fill="both", expand=True)


columns = ("Subject", "Marks", "Performance")

tree = ttk.Treeview(
    report_card,
    columns=columns,
    show="headings",
    height=6
)

tree.heading("Subject", text="Subject")
tree.heading("Marks", text="Marks")
tree.heading("Performance", text="Performance")

tree.column("Subject", width=250, anchor="center")
tree.column("Marks", width=180, anchor="center")
tree.column("Performance", width=250, anchor="center")

tree.pack(fill="both", expand=True)


# =========================
# STATUS
# =========================

status_label = tk.Label(
    root,
    text="Ready",
    anchor="w",
    font=("Segoe UI", 9),
    bg="#E9EEF5",
    fg="#555555",
    padx=15,
    pady=5
)
status_label.pack(fill="x")


# =========================
# CALCULATE FUNCTION
# =========================

def calculate_performance():

    try:
        name = name_entry.get().strip()
        roll = roll_entry.get().strip()
        semester = semester_entry.get().strip()

        if not name or not roll or not semester:
            messagebox.showerror(
                "Missing Information",
                "Please enter student name, roll number and semester."
            )
            return

        marks = {}

        for subject in SUBJECTS:
            value = float(mark_entries[subject].get())

            if value < 0 or value > 100:
                raise ValueError(
                    f"Marks for {subject} must be between 0 and 100."
                )

            marks[subject] = value

        total_classes = int(total_entry.get())
        attended_classes = int(attended_entry.get())

        if total_classes <= 0:
            raise ValueError("Total classes must be greater than 0.")

        if attended_classes < 0 or attended_classes > total_classes:
            raise ValueError(
                "Attended classes must be between 0 and total classes."
            )

        previous_text = previous_gpa_entry.get().strip()

        previous_gpas = []

        if previous_text:
            for value in previous_text.split(","):
                gpa_value = float(value.strip())

                if gpa_value < 0 or gpa_value > 10:
                    raise ValueError(
                        "GPA values must be between 0 and 10."
                    )

                previous_gpas.append(gpa_value)

        # Calculations
        total_marks = sum(marks.values())
        percentage = total_marks / len(SUBJECTS)

        grade = calculate_grade(percentage)
        current_gpa = grade_point(grade)

        cgpa = calculate_cgpa(
            previous_gpas,
            current_gpa
        )

        attendance = (
            attended_classes / total_classes
        ) * 100

        # Summary cards
        summary_labels["Percentage"].config(
            text=f"{percentage:.2f}%"
        )

        summary_labels["Grade"].config(
            text=grade
        )

        summary_labels["GPA"].config(
            text=f"{current_gpa:.1f}"
        )

        summary_labels["CGPA"].config(
            text=f"{cgpa:.2f}"
        )

        summary_labels["Attendance"].config(
            text=f"{attendance:.2f}%"
        )

        # Clear old table
        for item in tree.get_children():
            tree.delete(item)

        # Insert new data
        for subject, mark in marks.items():

            performance = subject_performance(mark)

            tree.insert(
                "",
                "end",
                values=(
                    subject,
                    f"{mark:.2f}",
                    performance
                )
            )

        status_label.config(
            text=f"Performance calculated successfully for {name}."
        )

        messagebox.showinfo(
            "Success",
            "Academic performance calculated successfully!"
        )

    except ValueError as error:

        messagebox.showerror(
            "Invalid Input",
            str(error)
        )


# =========================
# CHART FUNCTION
# =========================

def view_chart():

    try:

        marks = {}

        for subject in SUBJECTS:
            value = float(mark_entries[subject].get())

            if value < 0 or value > 100:
                raise ValueError(
                    f"Invalid marks for {subject}."
                )

            marks[subject] = value

        plt.figure(figsize=(9, 5))

        bars = plt.bar(
            marks.keys(),
            marks.values()
        )

        plt.title(
            "Subject-wise Academic Performance",
            fontsize=15,
            fontweight="bold"
        )

        plt.xlabel("Subjects")
        plt.ylabel("Marks")

        plt.ylim(0, 100)

        for bar, value in zip(bars, marks.values()):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                value + 2,
                f"{value:.0f}",
                ha="center",
                fontweight="bold"
            )

        plt.tight_layout()

        plt.savefig(
            "performance_chart.png",
            dpi=150,
            bbox_inches="tight"
        )

        plt.show()

        status_label.config(
            text="Performance chart displayed successfully."
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid marks for all subjects."
        )


# =========================
# CLEAR FUNCTION
# =========================

def clear_all():

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)

    total_entry.delete(0, tk.END)
    attended_entry.delete(0, tk.END)
    previous_gpa_entry.delete(0, tk.END)

    for entry in mark_entries.values():
        entry.delete(0, tk.END)

    for item in tree.get_children():
        tree.delete(item)

    for label in summary_labels.values():
        label.config(text="--")

    status_label.config(text="Ready")


# =========================
# BUTTONS
# =========================

calculate_button = tk.Button(
    button_frame,
    text="CALCULATE PERFORMANCE",
    command=calculate_performance,
    bg="#2F80ED",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=18,
    pady=9,
    cursor="hand2"
)

calculate_button.pack(side="left", padx=5)


chart_button = tk.Button(
    button_frame,
    text="VIEW CHART",
    command=view_chart,
    bg="#27AE60",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=18,
    pady=9,
    cursor="hand2"
)

chart_button.pack(side="left", padx=5)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_all,
    bg="#F2994A",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=18,
    pady=9,
    cursor="hand2"
)

clear_button.pack(side="right", padx=5)


exit_button = tk.Button(
    button_frame,
    text="EXIT",
    command=root.destroy,
    bg="#EB5757",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=18,
    pady=9,
    cursor="hand2"
)

exit_button.pack(side="right", padx=5)


# =========================
# START APPLICATION
# =========================

root.mainloop()