"""
Find Max
Infinity
The built-in float() function can create a numeric floating point value of negative infinity. Because every value will be greater than negative infinity, we can use it to help us accomplish our goal of finding the max value.

negative_infinity = float("-inf")
positive_infinity = float("inf")
Copy icon
Assignment
Our players want a way to see their strongest attack from their last combat. Let's add another function to analyze data from our combat log.

Complete the find_max function that looks at each number in the nums list and returns the maximum value. If no maximum is found, it just returns negative infinity. I've added it for you as the starting value of max_so_far.

For example:

max_val = find_max([100, 10, 22])
print(max_val)
# 100
Copy icon
Tip
max_so_far is just that, the highest number from the list so far. It starts as negative infinity because any and every number is larger than negative infinity.
"""

def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    
    return max_so_far
