
student_marks = {
    "Lalit": 85,
    "Raja": 92,
    "Subha": 78,
    "Mahesh": 88,
    "Eve": 95
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")