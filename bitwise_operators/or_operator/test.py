from main import *

submit_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
    (0b0000, 0b0000, 0b0000, 0b1011, 0b1011),
    (0b1001, 0b0010, 0b1101, 0b1011, 0b1111),
]

def test(input1,input2,input3,input4,e_o):
    print(f"Inputs: {input1}, {input2},{input3},{input4}")
    print(f"Expected output: {e_o}")

    result = calculate_guild_perms(input1,input2,input3,input4)

    print(f"Actual output: {result}")

    if(e_o == result):
        print("pass")
    else:
        print("fail")


def main():
    for test_case in test_cases:
        test(*test_case)

test_cases = submit_cases

main()
    