def convert(temperature, unit):
    if(unit == "C"):
        new_temperature = (180/100) * temperature + 32
        return new_temperature
    elif(unit == "F"):
        new_temperature = (100/180) * (temperature - 32)
        return new_temperature
    else:
        return "invalid unit"
    

print(convert(212, 'F'))
