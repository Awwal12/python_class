# You are tasked with writing a program that asks the user to input a number and prints out the result of the number squared. However, the program should also handle the following exceptions:

# If the user inputs a non-numeric value, the program should print an error message and ask the user to input a valid number.
# If the user inputs a negative number, the program should print an error message and ask the user to input a positive number.
# Write a Python program that implements the above requirements. Your program should use the try and except statements to catch and handle the exceptions. The program should keep asking the user for input until a valid number is provided, and then print out the squared result.
class NotPositiveError(UserWarning):
    pass


def main():
    while True:
        try:
            num = int(input('Input a number to be squared: '))
            # assert (num > 0), 'Number must be bigger than 0'
            if num <= 0:
                raise NotPositiveError
            else:
                result = num**2
            print(result)
        except ValueError:
            print("please input a numeric value")
        except NotPositiveError:
            print("Please input a positive number")


main()
