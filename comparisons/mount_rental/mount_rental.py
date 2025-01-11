def check_mount_rental(time_used,time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    
    return "no charges yet"

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
        print(f"Total {total}")
    return total

sum_of_odd_numbers(10)

def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance >3:
        current_health += 1
        enemy_distance -= 2
    
    print(f"current Health: {current_health}")

regenerate(9,10,3)

def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0  # Initialize total damage to 0
    
    for i in range(num_attacks):
        if i == num_attacks-1:
            total_damage += 4 * base_damage
            return total_damage
        
        total_damage += 2 * base_damage



result = calculate_flurry_crit(3,15)
print(f"Result: {result}")
