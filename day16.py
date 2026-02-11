def has_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return (count)
x = has_even([4,5,6,7])

if x >= 1:
    print("True")
else:
    print("False")
        