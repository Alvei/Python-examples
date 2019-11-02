""" Test the class_student. """
import unittest, datetime

from student.student import Person

class TestPerson(unittest.TestCase):
    def test_init_Person(self):
        mili, bob = Person('Mili Chad'), Person('Bob Paradis')
        zoe, anabel = Person('Zoe Lalonde'), Person('Potter')

        mili.set_birthday(datetime.date(1969, 5, 22))
        bob.set_birthday(datetime.date(1968, 7, 9))

        self.assertEqual(mili.name, 'Mili Chad')
        self.assertEqual(anabel.name, 'Potter')
        self.assertEqual(zoe.last_name, 'Lalonde')
        self.assertEqual(mili.birthday, datetime.date(1969, 5, 22))
        self.assertEqual(anabel.birthday, None)

    def test_getter_Person(self):
        mili, bob = Person('Mili Chad'), Person('Bob Paradis')
        zoe, anabel = Person('Zoe Lalonde'), Person('Potter')

        mili.set_birthday(datetime.date(1969, 5, 22))
        bob.set_birthday(datetime.date(1968, 7, 9))

        self.assertEqual(mili.get_name(), 'Mili Chad')
        self.assertEqual(anabel.get_last_name(), 'Potter')
        self.assertEqual(zoe.get_last_name(), 'Lalonde')
        self.assertEqual(bob.get_age(), (datetime.date.today() - datetime.date(1968, 7, 9)).days)


if __name__ == "__main__":
    unittest.main()
