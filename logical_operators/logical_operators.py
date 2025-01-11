"""

Logical Operators
You're probably familiar with the logical operators and and or.

Logical operators deal with boolean values, True and False.

The logical and operator requires that both inputs are True to return True. The logical or operator only requires that at least one input is True to return True.

For example:

True and True == True
True and False == False
False and False == False

True or True == True
True or False == True
False or False == False
Copy icon
Python Syntax
print(True and True)
# prints True

print(True or False)
# prints True
Copy icon
Nesting with parentheses
We can nest logical expressions using parentheses.

print((True or False) and False)
Copy icon
First, we evaluate the expression in the parentheses, (True or False). It evaluates to True:

print(True and False)
Copy icon
True and False evaluates to False:

print(False)
Copy icon
So, print((True or False) and False) prints "False" to the console.

"""

# not operator

"""
Not
We skipped a very important logical operator - not. The not operator reverses the result. It returns False if the input was True and vice-versa.

print(not True)
# Prints: False

print(not False)
# Prints: True
"""