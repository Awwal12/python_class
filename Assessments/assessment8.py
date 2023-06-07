# Question 5: Write a function that takes a list of numbers as input and returns the largest number in the list. Do not use the built-in max function.
def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(largest_number([2, 3, 64, 64, 12, 95]))
