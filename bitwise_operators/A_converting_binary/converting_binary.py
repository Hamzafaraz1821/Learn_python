def binary_string_to_int(num_servers, num_players, num_admins):
    data_a = int(num_servers,2)
    data_b = int(num_players,2)
    data_c = int(num_admins,2)

    return data_a,data_b,data_c

data_a, data_b, data_c = binary_string_to_int("100", "101", "110")
print(data_a)
# 4
print(data_b)
# 5
print(data_c)
# 6

attack_roll = 2
armor_class = 1

check = (attack_roll != 1 and attack_roll >= armor_class) or (attack_roll == 20)

print(check)