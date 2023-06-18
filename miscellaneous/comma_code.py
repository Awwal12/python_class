# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to
def comma_code(lst):
    if len(lst) == 1:
        return lst[0]
    return '{}, and {}'.format(', '.join(lst[:-1]), lst[-1])


lst = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(lst))
