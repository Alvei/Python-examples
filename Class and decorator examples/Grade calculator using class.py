""" Implementation of grade calculators using classes and decorators.
Created on Tue Jan 13 21:34:02 2015"""

# Dictionary to convert grades
L2G = {"A+": 4.3, "A": 4, "A-": 3.7,
       "B+": 3.3, "B": 3, "B-": 2.7,
       "C+": 2.3, "C": 2}


class Course():
    def __init__(self, name, grade=None, honor=False):
        self.__name = name
        self.__grade = grade
        self.__honor = honor

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    @property
    def honor(self):
        return self.__honor

    @honor.setter
    def honor(self, honor):
        self.__honor = honor

    def convert_grade(self):
        """ Convert the letter grades into numbers."""
        return L2G[self.grade]

    def __str__(self):
        if self.honor:
            ls = self.__name + "\t" + "Hon:\t" + str(self.__grade)
        else:
            ls = self.__name + "\t" + "Reg:\t" + str(self.__grade)
        return ls


def get_numerical_grades(courses):
    """ For the list of courses get the numerical grades.
        Signature: (list str) -> list of float."""
    letters = []

    for course in courses:
        letters.append(course.convert_grade())
    return letters


def average(numbers):
    """ Assumes numbers is a non empty list
        Returns the average of the list """

    try:   # Check for divide by zero error
        return sum(numbers) / float(len(numbers))
    except ValueError:
        raise ValueError("Unable to calculate average -> list is empty")


def main():
    """ Main code """

    # def TestGradeAverage():
    mathC = Course("Math", "A-", True)
    bioC = Course("BIOL", "A-")
    englishC = Course("English", "A-", True)
    spanishC = Course("Spanish", "B+")
    APUSHC = Course("APUSH", "B", True)
    CSC = Course("CSCI", "B+")

    courses = [mathC, bioC, englishC, spanishC, APUSHC, CSC]

    for course in courses:
        print(course)

    numbers = get_numerical_grades(courses)

    # print numbers
    print("GPA: {0:.2f}".format(average(numbers)))


if __name__ == '__main__':
    main()
