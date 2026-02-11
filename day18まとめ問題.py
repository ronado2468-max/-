def sum_odd(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 1:
            total += n
    return total
result = sum_odd([1,3,5,2,8])
print(result)

def is_odd_sum_big(numbers):
    total = sum_odd(numbers)
    if total >= 15:
        return "YES"
    else:
        return "NO"
result = is_odd_sum_big([1,3,5,2,8])
print(result) 