""" Simple grade book for classes
    Class Hiearchy: Person -> MIT_Person -> Student -> UG or Grad -> None
                    Grades -> None
"""
import datetime
from typing import Optional, List, Dict

class Person():
    """ Basic person object. """
    def __init__(self, name: str):
        """Create a person. """
        self.name = name

        # find the index of the last space from the end
        try:
            last_blank = name.rindex(' ')
            self.last_name: str = name[last_blank + 1:]
        except:
            self.last_name = name

        self.birthday: Optional[datetime.date] = None

    def get_name(self) -> str:
        """ Return self's full name"""
        return self.name

    def get_last_name(self) -> str:
        """Return self's las name"""
        return self.last_name

    def set_birthday(self, birthdate: Optional[datetime.date]) -> None:
        """ Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def get_age(self) -> int:
        """ Returns self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other) -> bool:
        """Returns True if self's name is lexicographically
           less than others's name, and False otherwise"""
        if self.last_name < other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name

    def __str__(self) -> str:
        return self.name


class MIT_Person(Person):
    """ MIT student class that uses Person class. """
    nextid_num = 0  # Identification number - class variable

    def __init__(self, name: str) -> None:
        """ Initialize. """
        Person.__init__(self, name)
        self.id_num = MIT_Person.nextid_num
        MIT_Person.nextid_num += 1

    def get_id_num(self) -> int:
        """ Getter function. """
        return self.id_num

    def __lt__(self, other) -> bool:
        """ Comparator. """
        return self.id_num < other.id_num

    def isstudent(self) -> bool:
        """ Uses built-in function to test type. """
        return isinstance(self, Student)

class Student(MIT_Person):
    """ Create a Student Class. Uses MIT_Person """

class UG(Student):
    """ University undergrad (UG) Student. Uses Class Student. """
    def __init__(self, name: str, class_year: int) -> None:
        """ Initializer function. """
        MIT_Person.__init__(self, name)
        self.year: int = class_year

    def get_class(self) -> int:
        """ Getter function. """
        return self.year

class Grad(Student):
    """ Create a Graduate Student Class. """

class Grades():
    """A mapping from students to a list of grades. """

    def __init__(self):
        """Create empty grade book. """
        self.students: List[Student] = []
        self.grades: Dict[int, list] = {}
        self.is_sorted: bool = True

    def add_student(self, student: Student):
        """Assumes: student is of type Student. Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.get_id_num()] = []
        self.is_sorted = False

    def add_grade(self, student: Student, grade: float) -> None:
        """ Add grade to the list of grades for student"""
        try:
            self.grades[student.get_id_num()].append(grade)
        except ValueError:
            raise ValueError('Student not in mapping')

    def get_grades(self, student):
        """ Return a list of grades for student"""
        try:  # Return copy of student's grades
            return self.grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')

    def get_students(self):
        """ Return the students in the grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True

        # Use generator, more memory efficient than passing a copy of a list
        for student in self.students:
            yield student


def grade_report(course: Grades) -> str:
    """ Returns a string with the name of all the students in the course."""
    report = '\nPrint mean grade for each student:'
    for student in course.get_students():
        tot = 0.0
        num_grades = 0
        # For a specific student calculate average
        for grade in course.get_grades(student):
            tot += grade
            num_grades += 1
        try:
            average = tot / num_grades
            report = report + '\n'\
                + str(student) + '\t' + str(round(average, 2))
        except ZeroDivisionError:
            report = report + '\n'\
                + str(student) + '\thas no grades'
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

def test_basic():
    """ Test Harness #1: Testing the Person Class. """
    print(f"\n****** Test 1: *******")
    mili, bob = Person('Mili Chad'), Person('Bob Paradis')
    zoe, anabel = Person('Zoe Lalonde'), Person('Anabel Potter')
    print(f"\n{mili}'s' last name is {mili.get_last_name()}")
    print(bob, mili, zoe, anabel)

    mili.set_birthday(datetime.date(1969, 5, 22))
    bob.set_birthday(datetime.date(1968, 7, 9))

    print(f"\n{mili.get_name()} is {mili.get_age()} days old")
    print(f"{bob.get_name()} is {bob.get_age()} days old")
    print(f"Bob was born {bob.get_age() - mili.get_age()} days before Mili")

def test_sorting():
    """ Test Harness #2: Testing the sorting using __lt__ and last name. """
    print(f"\n***** Test 2 *****")
    mili = Person('Mili Chad')
    bob = Person('Bob Paradis')
    zoe = Person('Zoe Lalonde')
    anabel = Person('Anabel Potter')
    roster = [zoe, mili, bob, anabel]

    for pers in roster:
        print(pers)
    print('\nSorted by last name')

    roster.sort()
    for pers in roster:
        print(pers)

def test_mit_class():
    """ Test Harness #3: Testing MIT_Person class and sorting based __Lt__ and  ID. """
    print(f"\n***** Test 3 *****")
    student1 = MIT_Person('Mark Guttag')
    student2 = MIT_Person('Billy Bob Beaver')
    student3 = MIT_Person('Billy Bob Beaver')
    student4 = Person('Billy Stephenson')   # Not an MIT student

    print(f"\n{student1}'s id number is {student1.get_id_num()}")
    print(f"{student2}'s id number is {student2.get_id_num()}")
    print(f"{student3}'s id number is {student3.get_id_num()}")

    print(f"\n{student1} < {student2} = {student1 < student2}")
    print(f"{student3} < {student2} = {student3 < student2}")
    print(f"{student4} < {student1} = {student4 < student1}")

    student5 = Grad('Buzz Aldrin')
    student6 = UG('Billy Beaver', 1984)
    print(f"\n{student5} is a graduate student is {isinstance(student5, Grad)}")
    print(f"{student6} is a an undergraduate student is {isinstance(student6, UG)}")

    print(f"\n{student5} is a student is {student5.isstudent()}")
    print(f"\n{student6} is a student is {student6.isstudent()}")
    print(f"\n{student3} is a student is {student3.isstudent()}")


def test_grades():
    """ Test Harness #4: Grade Book. """
    print(f"\n***** Test 4 *****")
    undergrad1 = UG('Jane Doe', 2014)
    undergrad2 = UG('John Doe', 2015)
    undergrad3 = UG('David Henry', 2003)
    grad1, grad2 = Grad('Billy Buckner'), Grad('Bucky F. Dent')

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


def main():
    """ Test harness. """
    #test_basic()
    #test_sorting()
    #test_mit_class()
    test_grades()

if __name__ == "__main__":
    main()
