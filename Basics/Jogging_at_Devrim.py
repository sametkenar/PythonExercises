""" Average speed given in meters per second"""

as1 = float(input())
dur1 = float(input())

as2 = float(input())
dur2 = float(input())

as3 = float(input())
dur3 = float(input())

as4 = float(input())
dur4 = float(input())

length_of_one_lap = float(input())


lap1 = as1 * dur1
lap2 = as2 * dur2
lap3 = as3 * dur3
lap4 = as4 * dur4

number_of_laps = (lap1 + lap2 + lap3 + lap4) / length_of_one_lap

print("{:.1f}".format(number_of_laps))