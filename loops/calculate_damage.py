def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0  # Initialize total damage to 0
    
    for i in range(num_attacks):
        if i == num_attacks-1:
            total_damage += 4 * base_damage
            return total_damage
        
        total_damage += 2 * base_damage



result = calculate_flurry_crit(3,15)
print(f"Result: {result}")

