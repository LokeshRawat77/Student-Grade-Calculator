# Student Grading System

# Function to determine grade and message
def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent Work! Keep shining! "
    elif marks >= 80:
        return "B", "Very Good! Keep it up! "
    elif marks >= 70:
        return "C", "Good Job! You can do even better! "
    elif marks >= 60:
        return "D", "Keep practicing and improving! "
    else:
        return "F", "Don't give up! Work harder and try again! "


# Get student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print(" Marks must be between 0 and 100.")
    except ValueError:
        print(" Please enter a valid number.")


# Get grade and message
grade, message = get_grade(marks)

# Display result
print("\n RESULT FOR", student_name.upper())
print("-" * 30)
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")