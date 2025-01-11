"""
Global Scope
So far we've been working in the global scope. That means that when we define a variable or a function, that name is accessible in every other place in our program, even within other functions.

For example:

pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius
Copy icon
Because pi was declared in the parent "global" scope, it is usable within the get_area_of_circle() function.

"""

# ?

# defined this variable = player_level in the global scope

player_level = 4

# Don't touch below this line


def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")
