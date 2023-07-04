# Define a class Student with the following attribute;
# name(String)
# age(integer)
# score (integer)
# 2. Create a file (name.txt) and add 10 name in each line
# 3. Use the open function to read from the file and get the names
# 4. Use the names gotten from the file to create a student object, using the names as attribute name, use the random package to create random ages from 16 – 19, and use the random package to add random scores from 20, 100
# 5. Create a method in Student to get the grade of the score;
# < 30 = F
# 30 – 40 = E
# 40 – 60 = C
# 60 – 70 = B
# 70  - 100= A
import random as r


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def grade(self):
        if self.score >= 70:
            print("A")
        elif self.score >= 60:
            print("B")
        elif self.score >= 50:
            print("C")
        elif self.score >= 30:
            print("E")
        elif self.score <= 29:
            print("F")


def getNames(filename):
    with open(filename, "r") as f:
        names = f.readlines()
    grades = []
    for student in names:
        grades.append(Student(student.split(',')[0], int(
            student.split(',')[1].strip('\n').strip(' '))))

    return grades


for grade in getNames('name.txt'):
    grade.grade()
    # print(grade)
