def sampled_average(numbers, k):
    n = len(numbers)
    if sum(numbers) - k * (n-1) in numbers:
        return "yes"
    else:
        return "no"
    

print(sampled_average([1,2,3,10],2))
print(sampled_average([1,3],2))