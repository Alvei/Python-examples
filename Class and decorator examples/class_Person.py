""" Simple grade book for classes
    for Python 3.5 """

import datetime


class Person(object):

    def __init__(self, name):
        """Create a person"""
        self.name = name

        # find the index of the last space from the end
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name

        self.birthday = None

    def getName(self):
        """Return self's full name"""
        return self.name

    def getLastName(self):
        """Return self's las name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Returns True if self's name is lexicographically
           less than others's name, and False otherwise"""
        if self.lastName < other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name


class MITPerson(Person):
    nextIdNum = 0  # Identification number - class variable

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def isStudent(self):
        return isinstance(self, Student)  # Uses built-in function to test type


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(Student):
    pass


class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:  # Return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    """original function
    def getStudents(self):
        #Return a list of the students in the grade book
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]   #Return a copy of the list of students """

    def getStudents(self):
        """Return the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True

        # Use generator, more memory efficient than passing a copy of a list
        for s in self.students:
            yield s


def gradeReport(course):
    """Assumes course is of type Grades
       Returns a string of students and their average grades"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        # For a specific student calculate average
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report = report + '\n'\
                + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n'\
                + str(s) + ' has no grades'
    return report


def printStudentList(course):
    """Assumes course is of type Grades
       Returns a string with all the names separated by \n"""
    report = ''

    for s in course.getStudents():
        report = report + '\n' + str(s)

    return report


def rawGradeReport(course):
    """Assumes course is of type Grades
       Returns a string of students and their grades"""

    report = ''
    for s in course.getStudents():
        report = report + str(s)
        for g in course.getGrades(s):

            report = report + '\t' + str(g)
        report = report + '\n'
    return report

# Test Harness #1: Testing the Person Class
#------------------------------------------


def test_basic():
    Mili = Person('Mili Choi')
    Hugo = Person('Hugo Sarrazin')
    Zoe = Person('Zoe Sarrazin')
    Anais = Person('Anais Potter')
    print(Mili, 'last name', Mili.getLastName())
    print(Hugo, Mili, Zoe, Anais)

    Mili.setBirthday(datetime.date(1969, 5, 22))
    Hugo.setBirthday(datetime.date(1968, 7, 9))
    print('\n')
    print(Mili.getName(), "is", Mili.getAge(), 'days old')
    print(Hugo.getName(), "is", Hugo.getAge(), 'days old')
    print('Hugo was born ', Hugo.getAge() - Mili.getAge(), ' days before Mili')

# Test Harness #2: Testing the sorting using __lt__ and last name
#---------------------------------------------------------------


def test_sorting():
    Mili = Person('Mili Choi')
    Hugo = Person('Hugo Sarrazin')
    Zoe = Person('Zoe Sarrazin')
    Anais = Person('Anais Potter')
    pList = [Zoe, Mili, Hugo, Anais]
    for p in pList:
        print(p)
    print('\nSorted by last name')
    pList.sort()
    for p in pList:
        print(p)

# Test Harness #3: Testing MITPerson class and sorting based __Lt__ and  ID
#---------------------------------------------------------------------------


def test_MITClass():
    p1 = MITPerson('Mark Guttag')
    p2 = MITPerson('Billy Bob Beaver')
    p3 = MITPerson('Billy Bob Beaver')
    p4 = Person('Billy Stephenson')

    print(str(p1) + '\'s id number is  ' + str(p1.getIdNum()))
    print(str(p2) + '\'s id number is  ' + str(p2.getIdNum()))
    print(str(p3) + '\'s id number is  ' + str(p3.getIdNum()))

    print('p1 < p2 = ', p1 < p2)
    print('p3 < p2 = ', p3 < p2)
    print('p4 < p1 = ', p4 < p1)

    p5 = Grad('Buzz Aldrin')
    p6 = UG('Billy Beaver', 1984)
    print(p5, 'is a graduate student is', type(p5) == Grad)
    print(p6, 'is a an undergraduate student is', type(p6) == UG)

    print(p5, 'is a student is ', p5.isStudent())
    print(p6, 'is a student is ', p6.isStudent())
    print(p3, 'is a student is ', p3.isStudent())

# Test Harness #4: Grade Book


def test_grades():
    ug1 = UG('Jane Doe', 2014)
    ug2 = UG('John Doe', 2015)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('Billy Buckner')
    g2 = Grad('Bucky F. Dent')
    sixHundred = Grades()
    sixHundred.addStudent(ug1)
    sixHundred.addStudent(ug2)
    sixHundred.addStudent(g1)
    sixHundred.addStudent(g2)

    # Go through the list of students (using the copy) and place 75 in the grade
    for s in sixHundred.getStudents():
        sixHundred.addGrade(s, 75)

    # Then add grades to a few
    sixHundred.addGrade(g1, 25)
    sixHundred.addGrade(g2, 100)
    sixHundred.addStudent(ug3)
    sixHundred.addGrade(g2, 90)
    print('\n ============>')

    # print printStudentList(sixHundred)
    print(rawGradeReport(sixHundred))
    print('\n')

    print(gradeReport(sixHundred))


# Testing
#============
# test_basic()
# test_sorting()
# test_MITClass()
test_grades()
