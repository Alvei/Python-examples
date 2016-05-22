
lloyd = {
    "name": "Lloyd",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
}
alice = {
    "name": "Alice",
    "homework": [100, 92, 98, 100],
    "quizzes": [82, 83, 91],
    "tests": [89, 97]
}
tyler = {
    "name": "Tyler",
    "homework": [0, 87, 75, 22],
    "quizzes": [0, 75, 78],
    "tests": [100, 100]
}
#Create a list of dictionaries
student = [lloyd, alice, tyler]


def averageList(inputList):
    ''' Function to calculate the average from a list
    Input: list of float or int
    Output: float'''
    total = sum(inputList)
    return float(total/len(inputList))

def get_average(studentInput):
    ''' Function to calculate the weighted average
    Input: dictionary
    Output: float of weighted average'''
    a1 = averageList(studentInput["homework"])
    a2 = averageList(studentInput["quizzes"])
    a3 = averageList(studentInput["tests"])
    wa = 0.1 * a1 + 0.3 * a2 + 0.6 * a3
    return wa

def get_letter_grade(score):
    ''' Function to convert a grade into a letter
    Input: float
    Output: string'''
    
    score = round(score)
    if score >= 90: return "A"
    if 80 <= score < 90: return "B"
    if 70 <= score < 80: return "C"
    if 60 <= score < 70: return "D"
    if score < 60: return "F"

def get_class_average(student):
    ''' Function that goes through all the list of student to calculate average
    Input: list of student dictionaries
    Output: float'''
    
    studentAverage = []
    
    for i in student:
        grade = get_average(i)
        studentAverage.append(grade)
        print "student", i['name'], "average = ", grade," ", get_letter_grade(grade)
        
    av = averageList(studentAverage)    
    return av

def main():
    av = get_class_average(student) #uses global list student
    print "class average =", av

main()
