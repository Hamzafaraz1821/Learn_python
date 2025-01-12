"""
List Operations - Contains
Checking whether a value exists in a list is also really easy in Python, just use the in keyword.

fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True
Copy icon
Assignment
Our players have requested an in-game feature that will allow them to type in a weapon name to check if it's in the list of top weapons in the realm.

Complete the is_top_weapon function. It should return True if the weapon is in the top_weapons list, otherwise it should return False.
"""

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    # don't touch above this line

    if weapon in top_weapons:
        return True
    else:
        return False