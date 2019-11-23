"""
Simple grade calculator. Need to enter both the unweighted and weighted grades.

Created on Tue Jan 13 19:39:10 2015

"""

# Dictionary to convert grades
L2G = {"A+": 4.3, "A": 4, "A-": 3.7,
       "B+": 3.3, "B": 3, "B-": 2.7,
       "C+": 2.3, "C": 2}

# List of grades unweighted
courses = {"Math": "A-", "BIO": "A-", "English": "A-",
           "Spanish": "B+", "CS": "A-", "APUSH": "B"}

# Weighted grades
coursesW = {"Math": "A-", "BIO": "A-", "English": "A",
            "Spanish": "B+", "CS": "A-", "APUSH": "B+"}


def convertGrade(courses, L2G):
    """ Simple function to convert class grades.
    Signature: (dict, dict) -> list """

    numerical_grades = []
    for course in courses:
        numerical_grades.append(L2G[courses[course]])
    return numerical_grades


def average(my_list):
    """ Calculate the average of a list.
        Signature: (list) -> list """

    try:   # Check for divide by zero error
        return sum(my_list) / float(len(my_list))
    except ValueError:
        raise ValueError("Unable to calculate average -> list is empty")


grades = convertGrade(courses, L2G)

GPA = average(grades)
print("Unweighted GPA:\t %.2f" % GPA)

grades_weigthed = convertGrade(coursesW, L2G)

GPAW = average(grades_weigthed)

print("Weighted GPA:\t %.2f" % GPAW)
