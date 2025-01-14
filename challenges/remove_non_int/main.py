"""
Remove Non-Integers
Complete the remove_nonints() function that takes a list and returns a new list with all the non-integer types removed.

remove_nonints(['1', 1, '3', '400', 4, 500])
# Remaining list after removing nonints = [1, 4, 500]
Copy icon
You can check the type of a variable using the type() function.

if type(variable) == int:
Copy icon
Do not change the input nums list, return a new list with only the integers.
"""

def remove_nonints(nums):
    int_removed = []
    for num in nums:
        if type(num) == int:
            int_removed.append(num)
    
    return int_removed