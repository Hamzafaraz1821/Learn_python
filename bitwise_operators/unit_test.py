# from bitwise_operators import *

# run_cases = [
#     (0b0110, False, True, True, False),
#     (0b1111, True, True, True, True),
#     (0b0000, False, False, False, False),
# ]

# submit_cases = run_cases + [
#     (0b1001, True, False, False, True),
#     (0b1000, True, False, False, False),
#     (0b0100, False, True, False, False),
#     (0b0010, False, False, True, False),
#     (0b0001, False, False, False, True),
# ]


# def test(
#     input1, expected_output1, expected_output2, expected_output3, expected_output4
# ):
#     print("---------------------------------")
#     print(f"Inputs: {input1:04b}")
#     print(f"Expecting can_create: {expected_output1}")
#     print(f"Expecting can_review: {expected_output2}")
#     print(f"Expecting can_delete: {expected_output3}")
#     print(f"Expecting can_edit: {expected_output4}")

#     result1 = get_create_bits(input1) == can_create_guild
#     result2 = get_review_bits(input1) == can_review_guild
#     result3 = get_delete_bits(input1) == can_delete_guild
#     result4 = get_edit_bits(input1) == can_edit_guild

#     print(f"Actual can_create: {result1}")
#     print(f"Actual can_review: {result2}")
#     print(f"Actual can_delete: {result3}")
#     print(f"Actual can_edit: {result4}")
#     if (
#         result1 == expected_output1
#         and result2 == expected_output2
#         and result3 == expected_output3
#         and result4 == expected_output4
#     ):
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()


from main import *

submit_cases = [
    (0b1000,True,False,False,False),
    (0b0100,False,True,False,False),
    (0b0010,False,False,True,False),
    (0b0001,False,False,False,True),
    (0b0110,False,True,True,False),
    ]

def test(input1,e_o1,e_o2,e_o3,e_o4):

    print(f"Inputs: {input1:04b}")
    print(f"E_O1: {e_o1}")
    print(f"E_O2: {e_o2}")
    print(f"E_O3: {e_o3}")
    print(f"E_O4: {e_o4}")

    r1 = get_create_bits(input1) == can_create_guild
    r2 = get_review_bits(input1) == can_review_guild
    r3 = get_delete_bits(input1) == can_delete_guild
    r4 = get_edit_bits(input1) == can_edit_guild

    print(f"Actual can_create {r1}")
    print(f"Actual can_review {r2}")
    print(f"Actual can_delete {r3}")
    print(f"Actual can_edit {r4}")

    if(
        r1 == e_o1,
        r2 == e_o2,
        r3 == e_o3,
        r4 == e_o4,
    ):
        print("pass")
    else:
        print("fail")


def main():

    for test_case in test_cases:
        test(*test_case)
    
    return None

test_cases = submit_cases

main()




