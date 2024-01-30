def best_food(coin):
    if coin == "HEADS":
        return "CALZONES"
    elif coin == "TAILS":
        return "WAFFLES"
    else:
        return "flip again"
    
print(best_food("NONE"))