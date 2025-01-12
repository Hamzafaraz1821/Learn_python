
def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance >3:
        current_health += 1
        enemy_distance -= 2
    
    print(f"current Health: {current_health}")

regenerate(9,10,3)