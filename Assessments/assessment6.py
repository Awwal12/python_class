# Question 3: Write a function that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the number of times each character appears in the string.
def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


input_string = "Hi my name is, what, my name is"
result = count_characters(input_string)
print(result)
