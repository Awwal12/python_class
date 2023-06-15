# write a function called "multiply_even_numbers" that takes in a list of numbers as parameters and returns the product of all even numbers, if there is no even numbers return 1.
def multiply_even_numbers(numbers):
    val = 1
    for x in numbers:
        if x % 2 == 0:
            val *= x
    return val


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(multiply_even_numbers(numbers))
