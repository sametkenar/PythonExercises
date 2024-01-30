int1 = int(input())
int2 = int(input())
int3 = int(input())

my_list = [int1, int2, int3]

min_value = min(my_list)
max_value = max(my_list)
mid_value = sum(my_list) - (min_value + max_value)

my_dict = {"min_val": min_value, "mid_val": mid_value, "max_val": max_value}


print(my_dict["min_val"],my_dict["mid_val"],my_dict["max_val"])