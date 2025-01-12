"""
Dictionaries
Dictionaries in Python are used to store data values in key -> value pairs. Dictionaries are a great way to store groups of information.

# use curly braces
# add key-value pairs
car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}
Copy icon
Here the car variable is assigned to a dictionary {} containing the keys brand, model and year. The keys' corresponding values are Tesla, 3 and 2019.

Assignment
Complete the get_character_record function. It takes a character's name, server, level, and rank as individual inputs, and returns a dictionary with the following string keys:

"name"
"server"
"level"
"rank"
"id"
Create and return a dictionary with the keys above. Assign each of the four inputs to the matching key, ie: "name": name.

Next, we can't have two characters named bloodwarrior123's on the same server! For the fifth key, id, create a unique value as follows:

Concatenate the name and the server inputs with a # in the middle. For example, given:

name = "bloodwarrior123"
server = "server1"
Then the id field would be set to bloodwarrior123#server1.

Tips
You can return the dictionary directly without first assigning it to a variable.
I recommend using an f-string to create the id field. This is a best practice.
"""

def get_character_record(name, server, level, rank):
    record = {
        "name" : name,
        "server" : server,
        "level" : level,
        "rank" : rank,
        "id" : f"{name}#{server}"
    }

    return record