def calculate_experience_points(level):
    total_XP = 0
    next_XP = 5

    for i in range(0,level):
        total_XP += next_XP * i

    print(f"Total XP: {total_XP}")    

calculate_experience_points(4)