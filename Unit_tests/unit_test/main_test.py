from Unit_tests.unit_test.main import *

run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = run_cases + [
    (0, 0, 0),
    (0, 200, 200),
]

def test(input1, input2, expected_output):
    print("----------------------------------")
    print(f"inputs = {input1}, input2 = {input2}")
    print(f"Expected output = {expected_output}")
    result = total_xp(input1, input2)
    if result == expected_output:
        print("Test passed")
        return True
    else:
        print("Test failed")
        return False
    
def main():
    passed_tests = 0
    failed_tests = 0

    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed_tests += 1
        else:
            failed_tests += 1
        
    if failed_tests == 0:
        print("All tests passed")
    else:
        print(f"{failed_tests} failed tests")

test_cases = submit_cases

if "__RUN__" in globals():
    test_cases = run_cases

main()