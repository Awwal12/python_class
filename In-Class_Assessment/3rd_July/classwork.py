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
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def getNames(self):
        with open('name.txt', "r") as f:
            names = list(f.readlines())
            return names

    def grade(self):
        self.score = r.randrange(20, 100)
        if self.score == 100 and 70:
            print("A")
        elif self.score == 60 and 69:
            print("B")
        elif self.score == 40 and 59:
            print("C")
        elif self.score == 30 and 49:
            print("E")
        elif self.score <= 29:
            print("F")
