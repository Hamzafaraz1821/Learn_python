def take_magic_damage(health, resist, amp, spell_power):
    new_health = health - (amp * spell_power - resist)
    return new_health