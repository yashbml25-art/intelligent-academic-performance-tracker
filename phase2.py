import matplotlib.pyplot as plt
# Intelligent Academic Performance Tracker & Visualizer

print("==============================================")
print("  ACADEMIC PERFORMANCE TRACKER & VISUALIZER")
print("==============================================")

# Student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
semester = input("Enter semester: ")

print("\nEnter Subject Details")
print("----------------------------------------------")

subjects = ["Python", "Java", "Mathematics", "DBMS", "English"]

# Function to calculate grade
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

# Function to calculate GPA
def grade_point(grade):
    if grade == "A+":
        return 10
    elif grade == "A":
        return 9
    elif grade == "B":
        return 8
    elif grade == "C":
        return 7
    elif grade == "D":
        return 6
    else:
        return 0

# Store marks
marks = {}

for subject in subjects:
    while True:
        mark = float(input(f"Enter marks for {subject}: "))

        if 0 <= mark <= 100:
            marks[subject] = mark
            break
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")

print("\nEnter Attendance Details")
print("----------------------------------------------")

while True:
    total_classes = int(input("Enter total classes: "))
    attended_classes = int(input("Enter attended classes: "))

    if total_classes > 0 and 0 <= attended_classes <= total_classes:
        break
    else:
        print("Invalid attendance! Please enter valid class values.")
# Calculate total and percentage
total_marks = sum(marks.values())
percentage = total_marks / len(subjects)

# Calculate grade
grade = calculate_grade(percentage)

# Calculate GPA
gpa = grade_point(grade)

# Calculate attendance
attendance_percentage = (attended_classes / total_classes) * 100

# Display report
print("\n==============================================")
print("           ACADEMIC PERFORMANCE REPORT")
print("==============================================")

print("Name       :", name)
print("Roll No.   :", roll_no)
print("Semester   :", semester)

print("\nSubject-wise Marks:")

for subject, mark in marks.items():
    print(f"{subject}: {mark}")
    print("\nSubject Performance Analysis:")

for subject, mark in marks.items():
    if mark >= 80:
        performance = "Strong"
    elif mark < 50:
        performance = "Weak"
    else:
        performance = "Average"

    print(f"{subject}: {performance}")

print("\nTotal Marks :", total_marks)
print("Percentage  :", round(percentage, 2), "%")
print("Grade       :", grade)
print("GPA         :", gpa)
print("Attendance  :", round(attendance_percentage, 2), "%")

print("==============================================")
# Generate subject-wise bar chart
plt.bar(marks.keys(), marks.values())

plt.title("Subject-wise Academic Performance")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.savefig("performance_chart.png")
print("Chart saved successfully as performance_chart.png")