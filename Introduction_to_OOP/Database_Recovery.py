def reinstall(data):
    entries = data.split(" |=| ")
    formatted_data = {}

    for entry in entries:
        key, value = entry.split(" : ")
        formatted_key = key.capitalize()
        formatted_value = int(value)
        formatted_data[formatted_key] = formatted_value

    return formatted_data

# Example Usage

input_data = "Entry-1 : 10 |=| Entry-2 : 20 |=| Entry-3 : 30"
result = reinstall(input_data)
print(result)

print(reinstall(" ahmet : 16 |=| Mehmet : 19 |=| selin : 32 |=| PINAR : 8 "))
print(reinstall(" SiLa : 2 |=| AbDuLlAh : 28 |=| PeLIN : 49 |=| PolaT : 99 "))
