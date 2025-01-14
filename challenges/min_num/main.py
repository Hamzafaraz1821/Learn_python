"""
Minimum Number in Python
Assignment
Write a function called find_min() that finds the smallest number in a list

find_min([1, 3, -1, 2]) -> -1

find_min([18, 3, 7, 2]) -> 2

Positive Infinity
Since you're trying to keep track of the smallest number, start with a really big number. Python has a built-in constant that represents positive infinity.

min = float("inf")
"""

def find_min(nums):
    min = float("inf")

    for i in nums:
        if i < min:
            min = i

    return min