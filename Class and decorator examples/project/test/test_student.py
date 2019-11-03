""" Test the class_student. """
import unittest, datetime

from student.student import Person, MIT_Person, UG, Grad, Grades

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.mili, self.bob = Person('Mili Chad'), Person('Bob Paradis')
        self.zoe, self.anabel = Person('Zoe Lalonde'), Person('Potter')

        self.mili.set_birthday(datetime.date(1969, 5, 22))
        self.bob.set_birthday(datetime.date(1968, 7, 9))
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_init_Person(self):
        self.assertEqual(self.mili.name, 'Mili Chad')
        self.assertEqual(self.anabel.name, 'Potter')
        self.assertEqual(self.zoe.last_name, 'Lalonde')
        self.assertEqual(self.mili.birthday, datetime.date(1969, 5, 22))
        self.assertIsNone(self.anabel.birthday)
        with self.assertRaises(TypeError):
            dan = Person(124)
            dan.set_birthday(1969)

    def test_getter_Person(self):
        self.assertEqual(self.mili.get_name(), 'Mili Chad')
        self.assertEqual(self.anabel.get_last_name(), 'Potter')
        self.assertEqual(self.zoe.get_last_name(), 'Lalonde')
        self.assertEqual(self.bob.get_age(), (datetime.date.today() - datetime.date(1968, 7, 9)).days)
        with self.assertRaises(ValueError):
            self.anabel.get_age()

    def test_lt_Person(self):
        self.assertLess(self.mili, self.bob)
        self.assertLess(self.zoe, self.anabel)

    def test_sorting(self):
        roster: list = [self.zoe, self.mili, self.bob, self.anabel]
        roster.sort()
        self.assertEqual(roster, [self.mili, self.zoe, self.bob, self.anabel])


class TestMITStudent(unittest.TestCase):
    def setUp(self):
        self.student1 = MIT_Person('Mark Guttag')
        self.student2 = MIT_Person('Billy Bob Beaver')
        self.student4 = Person('Billy Stephenson')   # Not an MIT student`
        self.student3 = MIT_Person('Billy Bob Beaver')
        self.student5 = Grad('Buzz Aldrin')
        self.student6 = UG('Billy Beaver', 1984)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_init_MIT_Person(self):
        # Student 4 is not from MIT so does not increment the id_num
        self.assertEqual(self.student1.name, 'Mark Guttag')
        self.assertEqual(self.student1.id_num, 0)
        self.assertEqual(self.student2.name, 'Billy Bob Beaver')
        self.assertEqual(self.student2.id_num, 1)
        self.assertEqual(self.student3.name, 'Billy Bob Beaver')
        self.assertEqual(self.student3.id_num, 2)
        self.assertEqual(self.student5.name, 'Buzz Aldrin')
        self.assertEqual(self.student5.id_num, 3)
        self.assertEqual(self.student6.name, 'Billy Beaver')
        self.assertEqual(self.student6.id_num, 4)
        self.assertEqual(self.student6.year, 1984)

    def test_lt_MIT_Person(self):
        # Uses the id_num to determine relative order
        self.assertLess(self.student1, self.student2)
        self.assertLess(self.student2, self.student3)
        self.assertGreater(self.student3, self.student2)

class TestGrades(unittest.TestCase):

    def test_Grades(self):
        self.undergrad1 = UG('Jane Doe', 2014)
        self.undergrad2 = UG('John Doe', 2015)
        self.undergrad3 = UG('David Henry', 2003)
        self.grad1, self.grad2 = Grad('Billy Buckner'), Grad('Bucky F. Dent')

        self.six_hundred = Grades()
        self.six_hundred.add_student(self.undergrad1)
        self.six_hundred.add_student(self.undergrad2)
        self.six_hundred.add_student(self.grad1)
        self.six_hundred.add_student(self.grad2)
        #self.assertIn(self.undergrad1, self.six_hundred.students)
        print("hi")

if __name__ == "__main__":
    unittest.main()
