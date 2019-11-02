""" Test the class_student. """
import unittest, datetime
from student import Person

class TestPerson(unittest.TestCase):
    def test_increasebday(self):
        mili, bob = Person('Mili Chad'), Person('Bob Paradis')
        zoe, anabel = Person('Zoe Lalonde'), Person('Anabel Potter')

        mili.set_birthday(datetime.date(1969, 5, 22))
        bob.set_birthday(datetime.date(1968, 7, 9))
        self.assertEqual(mili.get_name(), 'Mili Chad')

if __name__ == "__main__":
    unittest.main()
