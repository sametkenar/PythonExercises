def health_bar(base_health, current_health, damage):
    remaining_health = current_health - damage

    if(remaining_health < 0):       # deciding if you are dead or not
        remaining_health = 0

    missing_health = base_health - remaining_health
    health_bar = "X"*remaining_health + "_"*missing_health

    return health_bar

print(health_bar(11,11,4))
print(health_bar(8,2,6))
