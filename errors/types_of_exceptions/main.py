"""
Different Types of Exceptions
We haven't covered classes and objects yet, which is what an Exception really is at its core. We'll go more into that in the course on object-oriented programming.

For now, what is important to understand is that there are different types of exceptions, and we can handle them differently depending on the situation. Some exceptions are more specific, like ZeroDivisionError or IndexError, and some are more general, like the base Exception.

Syntax
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)
Copy icon
Which will print:

0 division
index error
Copy icon
Why Specific Exceptions Come First
When handling exceptions, it’s important to catch the most specific ones first, because Python stops checking once it finds a matching exception handler. If you catch a more general Exception first, any specific errors will never get handled individually.

For example:

try:
    nums = [0, 1]
    print(nums[2])
except Exception:
    print("An error occurred")
except IndexError:
    print("Index error")
Copy icon
In this case, the general Exception will catch the error before the IndexError can be reached, and the message “Index error” will never be printed. Always handle the most specific exception first!

Alias Exception Messages
As seen in the example, you can also access the error using as, like this:

except Exception as e:
    print(e)
Copy icon
The default behavior of print is that it will print the string representation of whatever object is passed to it. In this case, it will print the error message.

Assignment
Take a look at the get_player_record function. It raises an exception for negative player_ids.

Complete the handle_get_player_record() function. It should return the result of get_player_record, but if an IndexError is raised, it will instead return the string: index is too high. Otherwise, if any other exception is raised return the error.
"""

def handle_get_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e

# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

