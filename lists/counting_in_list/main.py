"""
Counting the Items in a List
Remember that we can iterate over all the elements in a list using a loop. For example, the following code will print each item in the sports list.

for i in range(0, len(sports)):
    print(sports[i])
Copy icon
Assignment
Our players need a way to see how many copies of a specific item they have within their inventory!

Let's finish the get_item_counts function. Within the loop, check if the items are a Potion, Bread, or Shortsword, then add up how many there are of each by incrementing the potion_count, bread_count and shortsword_count variables respectively.

Tip
The example shows you how to access the values in a list. Combine this with what you know about comparison and assignment operators to complete the assignment.
"""

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        item = items[i]
        if item == "Potion":
            potion_count += 1
        elif item == "Bread":
            bread_count += 1
        elif item == "Shortsword":
            shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count
