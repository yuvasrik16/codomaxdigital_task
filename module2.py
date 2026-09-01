"""
Task2.py
Module 2 - Python Mini Project: Student Grade Calculator

Features:
- Enter a student's name and marks for multiple subjects
- Calculates total, average, and letter grade
- Supports checking multiple students in one run
- Input validation with try/except

Run with:
    python Task2.py
"""


def get_grade(average):
    """Return a letter grade based on average marks (out of 100)."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def get_remark(grade):
    """Return a short remark based on the grade."""
    remarks = {
        "A+": "Outstanding!",
        "A": "Excellent!",
        "B": "Good job!",
        "C": "Fair, needs improvement.",
        "D": "Passed, but work harder.",
        "F": "Failed, needs serious improvement."
    }
    return remarks.get(grade, "")


def get_subject_marks():
    """Prompt user for number of subjects and marks for each; return list of marks."""
    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects <= 0:
                print("Please enter a number greater than 0.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    marks = []
    for i in range(1, num_subjects + 1):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i} (out of 100): "))
                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100.\n")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a number.\n")

    return marks


def calculate_result(marks):
    """Return total, average, and grade for a list of marks."""
    total = sum(marks)
    average = total / len(marks)
    grade = get_grade(average)
    return total, average, grade


def print_report(name, marks, total, average, grade):
    """Print a formatted grade report card."""
    print("\n" + "=" * 40)
    print(f"GRADE REPORT: {name}")
    print("=" * 40)
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark}/100")
    print("-" * 40)
    print(f"Total Marks : {total}/{len(marks) * 100}")
    print(f"Average     : {average:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Remark      : {get_remark(grade)}")
    print("=" * 40 + "\n")


def student_grade_calculator():
    print("=" * 40)
    print("   STUDENT GRADE CALCULATOR")
    print("=" * 40)
    print("Type 'quit' as the student name to exit.\n")

    students = []  # store results for a summary at the end

    while True:
        name = input("Enter student name: ").strip()

        if name.lower() == "quit":
            break

        if not name:
            print("Name cannot be empty.\n")
            continue

        marks = get_subject_marks()
        total, average, grade = calculate_result(marks)
        print_report(name, marks, total, average, grade)

        students.append((name, average, grade))

    # Final summary of all students checked in this session
    if students:
        print("\n" + "#" * 40)
        print("SESSION SUMMARY")
        print("#" * 40)
        for name, average, grade in students:
            print(f"{name}: {average:.2f}% -> Grade {grade}")
        print("#" * 40)

    print("\nGoodbye!")


if __name__ == "__main__":
    student_grade_calculator()