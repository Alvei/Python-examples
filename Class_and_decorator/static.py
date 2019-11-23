""" static.py

Example of using @staticmethod and @classmethod
Created on Sat Mar 10 15:36:19 2018
http://stackabuse.com/understanding-pythons-yield-keyword/
"""


class ClassGrades:

    def __init__(self, grades):
        self.grades = grades

    @classmethod
    def from_csv(cls, grade_csv_str):
        # take the string that is csv and separate usign map function
        grades = list(map(int, grade_csv_str.split(', ')))

        cls.validate(grades)    # call static method()
        return cls(grades)      # return the cls object which is a class object

    @staticmethod
    def validate(grades):
        for g in grades:
            if g < 0 or g > 100:
                raise Exception()

def main():
    try:
        # Try out some valid grades
        class_grades_valid = ClassGrades.from_csv('90, 80, 85, 94, 70')
        print(f"Got grades: {class_grades_valid.grades}")

        # Should fail with invalid grades
        class_grades_invalid = ClassGrades.from_csv('92, -15, 99, 101, 77, 65, 100')
        print(class_grades_invalid.grades)
    except:
        print('Invalid!')

if __name__ == "__main__":
    main()