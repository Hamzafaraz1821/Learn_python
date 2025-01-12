"""
Find an Item in a List
Practice the "no-index" or "no-range" syntax:

for fruit in fruits:
    print(fruit)
Copy icon
Assignment
We need to check if a player has a specific item in their inventory. In the contains_leather_scraps function, use the no-index syntax to iterate over each item in items. If you find an item called Leather Scraps, set the found variable to True.
"""

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    # ?
    for item in items:
        if item == "Leather Scraps":
            found = True
            break

    # don't touch below this line

    return found