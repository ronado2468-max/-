def gusu_number(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return (count)
result = gusu_number([1,2,3,4,5])
print(result)