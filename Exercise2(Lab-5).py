students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],
    [206, "Karim", [75, 75, 75]],
    [207, "Sadia", [70, 70, 70]],
    [208, "Rafi", [70, 70, 70]],
    [209, "Nila", [80, 105, 90]],
    [210, "Mina", []]
]


def calculate_average(marks):
    if len(marks) == 0:
        return None

    for mark in marks:
        if mark < 0 or mark > 100:
            return None

    return sum(marks) / len(marks)


def classify_performance(average):
    if average is None:
        return "Invalid or Missing Marks"
    elif average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]

        average = calculate_average(marks)
        performance = classify_performance(average)

        print("ID:", student_id)
        print("Name:", name)

        if average is None:
            print("Average: Not available")
        else:
            print("Average:", round(average, 2))

        print("Performance:", performance)


display_report(students)