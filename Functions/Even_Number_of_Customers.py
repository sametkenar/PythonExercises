counter = 0

def incoming():
    global counter
    counter +=1

def outgoing():
    global counter
    if counter > 0: counter -=1

def even_customers():
    return counter % 2 == 0

