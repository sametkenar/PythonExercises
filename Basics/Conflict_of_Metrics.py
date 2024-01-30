mile_distance = int(input())
kmh_speed = int(input())

kmh_distance = mile_distance * 1.6
# multiplied with 60 due to time in minutes
time = (kmh_distance / kmh_speed) * 60 
print("{:.2f}".format(time))