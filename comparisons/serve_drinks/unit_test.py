from should_serve_drinks import *

test_cases = [
    (22,False,6, True),
    (21,True,6, False),
    (22,False,3, False),
    (18,False,6, False),
]

def test(age,on_break,time,expected_result):
    print(f"Age: {age}, On break? {on_break}, Time: {time}")
    print(f"Expected result: {expected_result}")
    result = should_serve_customer(age,on_break,time)
    print(f"Actual result: {result}")

    if result == expected_result:
        print("pass")
    else:
        print("fail")
    
def main():
    for test_case in test_cases:
        test(*test_case)

main()