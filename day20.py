def average_positive(numbers):
    total = 0
    count = 0
    for n in numbers:
        if n > 0:
            total += n
            count += 1
    return total / count
result = average_positive([1,-2,3,0,6])
print(result)
    
def average_positive_safe(numbers):
    total = 0
    count = 0
    for n in numbers:
        if n > 0:
            total += n
            count += 1

    if count == 0:
        return "NONE"
    else:
        return total / count
result = average_positive_safe([1,-3,0])
print(result)
