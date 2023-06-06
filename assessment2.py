# Write a Python function called largest_divisible that takes two arguments, an integer n and a list of integers lst, and returns the largest integer in lst that is divisible by n. Your function should use a loop and an if statement to identify integers in lst that are divisible by n, and should return the largest such integer. If no integers in lst are divisible by n, your function should return None.

# Here's an example input and output to help clarify what your function should do:

# 	numbers = [10, 12, 15, 16, 20, 22]
# 	n = 4
# 	print(largest_divisible(n, numbers)) # Output: 20


# Explanation: In the input list [10, 12, 15, 16, 20, 22], the integers that are divisible by 4 are 12, 16, and 20. The largest of these integers is 20, which is the output of the largest_divisible function.

# If there are no integers in the list that are divisible by n, the function should return None. For example:

# 	numbers = [1, 3, 5, 7]
# 	n = 2
# 	print(largest_divisible(n, numbers)) # Output: None
numbers = [10, 12, 15, 16, 20, 22]
n = 2


def largest_divisible(n, lst):
    lsst = []
    for i in lst:
        if i % n == 0:
            lsst.append(i)
        else:
            continue
    if len(lsst) == 0:
        return None
    print(max(lsst))


largest_divisible(n, numbers)
