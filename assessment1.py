# 1. Write a function called grade_average that takes a list of grades (integers) as input and returns the average grade as a letter grade (string). Your function should use a loop and an if statement to calculate the average grade and then convert it to a letter grade based on the following scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# Your function should round the average grade to the nearest integer before converting it to a letter grade.
score1 = float(input('pls input your maths score:'))
score2 = float(input('pls input your english score:'))
score3 = float(input('pls input your econs score:'))
score4 = float(input('pls input your f-maths score:'))
score5 = float(input('pls input your biol score:'))
score6 = float(input('pls input your physics score:'))
Totalscores = [score1, score2, score3, score4, score5, score6]


def grade_average(*args):

    for i in args:
        totalSum = sum(i)
        avg = round(totalSum / len(i))
        if avg >= 90 and avg <= 100:
            print(f"A: {avg}")
        elif avg == 80 and avg <= 89:
            print(f"B: {avg}")
        elif avg == 70 and avg <= 79:
            print(f"C: {avg}")
        elif avg == 60 and avg <= 69:
            print(f"D: {avg}")
        elif avg <= 59:
            print(f"F: {avg}")


grade_average(Totalscores)
