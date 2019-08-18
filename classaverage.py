
""" Simple example to calculate averages across a dictionary
"""


def list_average(inputList):
    ''' Function to calculate the average from a list
        Signature: (list) -> float.'''
    total = sum(inputList)
    return float(total / len(inputList))


def get_average(student_input):
    ''' Function to calculate the weighted average
        Signature: (dictionary) -> float.'''
    weight = [0.1, 0.3, 0.6]
    a1 = list_average(student_input["homework"])
    a2 = list_average(student_input["quizzes"])
    a3 = list_average(student_input["tests"])
    wa = weight[0] * a1 + weight[2] * a2 + weight[3] * a3
    return wa


def letter_grade(score):
    ''' Function to convert a grade into a letter
        Signature: (float) -> string.'''

    score = round(score)

    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    return "F"


def class_average(students):
    ''' Function that goes through all the list of student to calculate average
        Signature(list of dictionaries) -> float.'''

    student_average = []

    for student in students:
        grade = get_average(student)
        student_average.append(grade)
        print("student", student['name'], "average = ", grade, " ", letter_grade(grade))

    return list_average(student_average)

# Test harness
# ############


def main():

    # Define data entry dictionaries
    lloyd = {
        "name": "Lloyd",
        "homework": [90, 97, 75, 92],
        "quizzes": [88, 40, 94],
        "tests": [75, 90]
    }
    alice = {
        "name": "Alice",
        "homework": [100, 92, 98, 100],
        "quizzes": [82, 83, 91],
        "tests": [89, 97]
    }
    tyler = {
        "name": "Tyler",
        "homework": [0, 87, 75, 22],
        "quizzes": [0, 75, 78],
        "tests": [100, 100]
    }

    # Create a list of dictionaries
    students = [lloyd, alice, tyler]

    av = class_average(students)
    print("class average =", av)


main()
