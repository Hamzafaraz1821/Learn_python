def get_most_common_enemy(enemies_dict):
    maxi = float("-inf")
    maxi_key = None
    for enemy in enemies_dict:
        count = enemies_dict[enemy]
        if count > maxi:
            maxi = count
            maxi_key = enemy
        
    return maxi_key

