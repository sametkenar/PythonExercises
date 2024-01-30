import math

# Input the width and length of the room
width = int(input("Enter the width of the room: "))
length = int(input("Enter the length of the room: "))

# Calculate the area of the room
area = width * length

# Calculate the maximum possible length of a tile
max_tile_length = math.gcd(width, length)

# Calculate the number of tiles required
num_tiles = area // (max_tile_length ** 2)

# Print the result
print("The minimum possible count of tiles required is:", num_tiles)