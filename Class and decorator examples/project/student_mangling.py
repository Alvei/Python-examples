""" Simple grade book for classes
    Class Hiearchy: Person -> Student -> UG or Grad -> None
                    Grades -> None
    Student has a class counter.
"""
import datetime
from typing import Optional, List, Dict

class Person():
    """ Basic person object. """
    def __init__(self, name: str):
        """ Create a Person. Must specify a name. """
        if not isinstance(name, str):
            raise TypeError(f"Person name:{name} is not a string but a {type(name)}")
        self.__name = name

        # find the index of the last space from the end
        try:
            last_blank = name.rindex(' ')
            self.__last_name: str = name[last_blank + 1:]
        except:
            self.__last_name = name

        self.__birthday: Optional[datetime.date] = None

    def get_name(self) -> str:
        """ Return self's full name"""
        return self.__name

    def get_last_name(self) -> str:
        """ Return self's las name"""
        return self.__last_name

    def set_birthday(self, birthdate: Optional[datetime.date]) -> None:
        """ Sets self's birthday to birthdate. """
        if not isinstance(birthdate, datetime.date):
            raise TypeError(f"Bday of:{self.__name} should be specificed as a {type(datetime.date)}")
        self.__birthday = birthdate

    def get_birthday(self) -> str:
        """ Return self's las name"""
        return self.__birthday

    def get_age(self) -> int:
        """ Returns self's current age in days. """
        if self.get_birthday() is None:
            raise ValueError
        return (datetime.date.today() - self.get_birthday()).days

    def __lt__(self, other) -> bool:
        """ Returns True if self's name is lexicographically
            less than others's name, and False otherwise. """
        if self.__last_name < other.__last_name:
            return True
        return False

    def __str__(self) -> str:
        """ Representation of the class. """
        return self.__name


class Student(Person):
    """ Student class that uses Person class but also has a unique ID. """
    nextid_num = 0  # Identification number - class variable

    def __init__(self, name: str) -> None:
        """ Initialize. """
        Person.__init__(self, name)
        self.__id_num = Student.nextid_num
        Student.nextid_num += 1

    def get_id_num(self) -> int:
        """ Getter function. """
        return self.__id_num

    def __lt__(self, other) -> bool:
        """ Comparator. """
        return self.get_id_num() < other.get_id_num()

    def isstudent(self) -> bool:
        """ Uses built-in function to test type. """
        return isinstance(self, Student)

class UG(Student):
    """ University undergrad (UG) Student. Uses Class Student. """
    def __init__(self, name: str, class_year: int) -> None:
        """ Initializer function. Year is graduation year. """
        Student.__init__(self, name)
        self.__year: int = class_year

    def get_class(self) -> int:
        """ Getter function. """
        return self.__year

class Grad(Student):
    """ Create a Graduate Student Class. Uses Class Student. """
    def __init__(self, name: str) -> None:
        """ Initializer function. """
        Student.__init__(self, name)

class Grades():
    """A gradebook with mapping from students to a list of grades. """

    def __init__(self) -> None:
        """Create empty grade book. """
        self.__students: List[Student] = []
        self.__grades: Dict[int, List[float]] = {}
        self.__is_sorted: bool = True

    def add_student(self, student: Student) -> None:
        """Assumes: student is of type Student. Add student to the grade book. """
        if student in self.__students:
            raise ValueError('Duplicate student')
        self.__students.append(student)
        self.__grades[student.get_id_num()] = []
        self.__is_sorted = False

    def get_students(self):
        """ Return the students in the grade book. """
        if not self.__is_sorted:
            self.__students.sort()
            self.__is_sorted = True

        # Use generator, more memory efficient than passing a copy of a list
        for student in self.__students:
            yield student

    def add_grade(self, student: Student, grade: float) -> None:
        """ Add grade to the list of grades for student. """
        try:
            self.__grades[student.get_id_num()].append(grade)
        except AttributeError:
            raise AttributeError('Student not in gradebook')

    def get_grades(self, student: Student) -> List[float]:
        """ Return a list of grades for student. """
        try:  # Return copy of student's grades
            return self.__grades[student.get_id_num()][:]
        except AttributeError:
            raise AttributeError('Student not in gradebook')

    def calculate_average(self, student: Student) -> float:
        """ Calculates the average of list of grades. """
        given_grades = self.get_grades(student)
        total: float = 0
        num_grades: int = 0
        # For a specific student calculate average
        for grade in given_grades:
            total += grade
            num_grades += 1

        # Calculate average
        try:
            average = total / num_grades
            return average
        except ZeroDivisionError:
            return -99.

def grade_report(course: Grades) -> str:
    """ Returns a string with the name of all the students in the course. """
    report = '\nPrint mean grade for each student:'
    for student in course.get_students():
        average = course.calculate_average(student)

        if average == -99:
            report = report + '\n'\
                + str(student) + '\thas no grades'
        else:
            report = report + '\n'\
                + str(student) + '\t' + str(round(average, 2))

    return report

def print_student_list(course: Grades) -> str:
    """ Returns a string with the name of all the students in the course. """
    report = '\nPrinting student list'
    for student in course.get_students():
        report = report + '\n' + str(student)
    return report

def raw_grade_report(course: Grades) -> str:
    """ Returns a string with the name of all the students & grades in the course."""
    report = '\nPrint raw grade report:\n'
    for student in course.get_students():
        report = report + str(student)
        for grade in course.get_grades(student):

            report = report + '\t' + str(grade)
        report = report + '\n'
    return report

def main():
    """ Test harness. """
    print(f"\n***** Test Gradebook *****")
    # Create undergrad and grad students
    undergrad1 = UG('Jane Doe', 2014)
    undergrad2 = UG('John Doe', 2015)
    undergrad3 = UG('David Henry', 2003)
    grad1, grad2 = Grad('Billy Buckner'), Grad('Bucky F. Dent')

    # Fill the gradbook
    six_hundred = Grades()
    six_hundred.add_student(undergrad1)
    six_hundred.add_student(undergrad2)
    six_hundred.add_student(grad1)
    six_hundred.add_student(grad2)

    # Go through the list of students (using the copy) and place 75 in the grade
    print("Enter grades:")
    for student in six_hundred.get_students():
        six_hundred.add_grade(student, 75)

    # Then add grades to a few students
    six_hundred.add_grade(grad1, 25)
    six_hundred.add_grade(grad2, 100)
    six_hundred.add_student(undergrad3)
    six_hundred.add_grade(grad2, 90)

    #print(print_student_list(six_hundred))
    print(raw_grade_report(six_hundred))
    print(grade_report(six_hundred))


if __name__ == "__main__":
    main()
