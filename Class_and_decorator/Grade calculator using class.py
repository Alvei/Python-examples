""" Implementation of grade calculators using classes and decorators. """
from typing import List

# Dictionary to convert grades
L2G = {"A+": 4.3, "A": 4, "A-": 3.7,
       "B+": 3.3, "B": 3, "B-": 2.7,
       "C+": 2.3, "C": 2}


class Course():
    def __init__(self, name: str, grade: str=None, honor: bool=False) -> None:
        """ Initialize. """
        self.__name = name
        self.__grade = grade
        self.__honor = honor

    @property
    def name(self) -> str:
        """ Getter. """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """ Setter. """
        self.__name = name

    @property
    def grade(self):
        """ Getter. """
        return self.__grade

    @grade.setter
    def grade(self, grade: str) -> None:
        """ Setter. """
        self.__grade = grade

    @property
    def honor(self) -> bool:
        """ Getter. """
        return self.__honor

    @honor.setter
    def honor(self, honor: bool):
        """ Setter. """
        self.__honor = honor

    def convert_grade(self) -> float:
        """ Convert the letter grades into numbers. """
        return L2G[self.__grade]

    def __str__(self) -> str:
        if self.__honor:
            class_type = "Hon"
        else:
            class_type = "Reg"
        ls = f"{self.__name}\t {class_type}:\t {str(self.__grade)}"
        return ls


def get_numerical_grades(courses: List[Course]) -> List[float] :
    """ For the list of courses get the numerical grades."""
    letters: List[float] = []

    for course in courses:
        letters.append(course.convert_grade())
    return letters


def average(numbers: List[float]) -> float:
    """ Assumes numbers is a non empty list. Returns the average of the list. """

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

    print(f"GPA: {average(numbers):.2f}")


if __name__ == '__main__':
    main()
