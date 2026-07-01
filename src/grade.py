"""
Student Grade Prediction System

This program accepts marks for five subjects,
calculates the average, and assigns a grade.

Author: Sakshi Gaonkar
"""

def calculate_average(marks):
    """Calculate the average of the given marks."""
    return sum(marks) / len(marks)


def grades(average):
    """Return grade based on average marks."""

    if average >= 90:
        return "A+"

    elif average >= 75:
        return "A"

    elif average >= 60:
        return "B"

    elif average >= 50:
        return "C"

    else:
        return "Fail"


def get_marks():
    """Read marks for five subjects with validation."""

    marks = []

    print("\nEnter marks for 5 subjects (0-100)\n")

    for i in range(1, 6):

        while True:

            try:
                mark = float(input(f"Subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return marks


def main():

    marks = get_marks()

    average = calculate_average(marks)

    grade = grades(average)

    print("\n------ Result ------")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")


if __name__ == "__main__":
    main()
