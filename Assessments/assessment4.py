# Question 1: Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list.
def sumsUp(numbers):
    result = 0
    for i in numbers:
        result += i
    return result


print(sumsUp([2, 3, 4, 43, 2, 4]))
