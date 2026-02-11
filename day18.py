def add(a,b):
    return a + b

x = add(3,5)
print(x + 10)

def sum_even(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total

result = sum_even([1,2,3,4,6])
print(result)

def is_even_sum_big(numbers):
    total = sum_even(numbers)
    if total >= 10:
        return "YES"
    else:
        return "NO"
result = is_even_sum_big([1,2,3,4,6])
print(result)