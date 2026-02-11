def sum_even(numbers):
    total = 0
    count = 0
    for n in numbers:
        if n > 0:
            total += n
            count += 1
    return total
    return count

def a_sum_even(numbers):
    total = sum_even(numbers)
    count = sum_even(numbers)
    if total >= 50 and count >= 5:
        return "EXCELLENT"
    elif total >= 20:
        return "GOOD"
    elif count >= 1:
        return "TRY"
    else:
        return "NONE"

def b_sum_even(numbers):
    total = sum_even(numbers)
    count = sum_even(numbers)
    return  a_sum_even(numbers)
result = b_sum_even([40,2,5,4,3,2])
print(result)

def gusu_even(numbers):
    result =[]
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
print(gusu_even([1,2,3,4,5,6]))

def jyuijyou_even(numbers):
    result = []
    for n in numbers:
        if n >= 10:
            result.append(n)
    return result
print(jyuijyou_even([10,4,5,20,40]))

def seikazu_even(numbers):
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)

    if len(result) >= 3:
        return "OK"
    else:
        return "NG"

print(seikazu_even([1,-2,3,4]))

    



