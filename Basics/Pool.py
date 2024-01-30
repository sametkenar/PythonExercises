# the capacities of faucets
f1 = int(input())
f2 = int(input())
f3 = int(input())
f4 = int(input())
f5 = int(input())

# depths of 4th and 5th faucets
d4 = int(input())
d5 = int(input())

# length, width and depth of the pool
l_p = int(input())
w_p = int(input())
d_p = int(input())

# heights of the fourth and fifth faucets from the bottom of the pool
h4 = d_p - d4
h5 = d_p - d5

# Time to fill the volume between the bottom up to height of fourth faucet
t1 = (h4 * w_p * l_p) / (f1 + f2 + f3)

# Time to fill the volume between the faucet four and five
t2 = ((h5 - h4)* w_p * l_p) /(f1 + f2 + f3 - f4)

# Time to fill the rest
t3 = ((d_p - h5) * w_p * l_p) / (f1 + f2 + f3 - f4 - f5)

print("Time to fill the pool is {:.1f} mins".format(t1 + t2 + t3))