import math

# Input the fuel tank capacity, fuel consumption per 100 km, and length of trip
tank_capacity = float(input("Enter the fuel tank capacity (liters): "))
fuel_consumption = float(input("Enter the fuel consumption per 100 km (liters): "))
trip_length = float(input("Enter the length of the trip (km): "))

# Calculate the total fuel required for the trip
total_fuel = (fuel_consumption / 100) * trip_length

# Calculate the number of times the truck needs to refill its tank
num_refills = math.ceil(total_fuel / tank_capacity)

# Calculate the remaining liters of fuel in the truck's tank at the end of the trip
remaining_fuel = tank_capacity * num_refills - total_fuel

# Print the output
print("Number of times to refill:", num_refills)
print("Remaining liters of fuel:", format(remaining_fuel, ".2f"))

