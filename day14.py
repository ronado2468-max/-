def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value
result = find_max([3,7,2,9,5])
print(result)
    
def find_small(numbers):
    small_value = numbers[0]
    for n in numbers:
        if n < small_value:
            small_value = n
    return small_value 
result = find_small([3,7,2,9,5])
print(result)

