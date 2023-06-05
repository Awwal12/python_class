# Write a function called find_common_elements that takes two lists as input and returns a new list that contains the common elements between the two lists. Your function should use a loop and an if statement to identify common elements, and should return the common elements in the order in which they appear in the first list.


# SOLUTION 1 uses lists as the data structure
# ran1 = [1, 2, 3, 4, 5]
# ran2 = [2, 5, 3, 6, 7]


# def find_common_elements(ran1, ran2):
#     ran3 = []
#     for i in ran1:
#         for j in ran2:
#             if i == j:
#                 ran3.append(i)
#     return ran3


# result = find_common_elements(ran1, ran2)
# print(result)


# SOLUTION 2 uses sets as a data structure
ran1 = {1, 2, 3, 4, 5}
ran2 = {2, 5, 3, 6, 7}
ran3 = set()


def find_common_elements(ran1, ran2):
    ran3 = ran1 & ran2
    return ran3


result = find_common_elements(ran1, ran2)
print(result)
