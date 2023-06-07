# Question 2: Write a function that takes a string and returns the amount of vowels in the string
def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count


print(vowel_count('governor'))
