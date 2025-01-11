from main import *

run_cases = [
    (100, 5, 2, 20, 65),
    (200, 10, 1, 25, 185),
]

submit_cases = run_cases + [
    (0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1),
    (100, 2, 3, 1, 99),
    (2500, 3, 2, 2, 2499),
]

def test(input1, input2, input3, input4, expected):
    print("--------------------------------------")
    print(f"inputs = {input1, input2, input3, input4}")
    result = take_magic_damage(input1, input2, input3, input4)
    if result == expected:
        print("PASSED")
        return True
    else:
        print("FAILED")
        print(f"Expected: {expected}, but got {result}")
        return False
    
def main():
    passed = 0
    failed = 0

    for test_case in test_cases: 
        if test(*test_case):
            passed += 1
        else:
            failed += 1
        
    print("--------------------------------------")
    print(f"Passed: {passed}, Failed: {failed}")

test_cases = submit_cases

main()