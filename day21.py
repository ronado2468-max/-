def sum_even(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total

def a_sum_even(total):
    if total >= 100:
        return "EXCELLENT"
    elif total >= 50:
        return "GOOD"
    elif total >= 1:
        return "OK"
    else:
        return "NONE"
    
def b_sum_even(numbers):
    total = sum_even(numbers)
    return a_sum_even(total)

result = b_sum_even([10,-5,20,3])
print(result)
    