# write a function called "count_positive_negative" that counts the number of positive and negative numbers in a list the function should return a tuple with two elements: a count of positive and negative numbers.
nums = [1, 2, -3, 4, -5, 5, 9, -1]


def count_positive_negative(nums):
    count_P = 0
    count_N = 0
    for x in nums:
        new_list = (count_P, count_N)
        if x > 0:
            count_P += 1
        elif x < 0:
            count_N += 1
    return new_list


print(count_positive_negative(nums))
