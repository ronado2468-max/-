def is_even(n):
    return n % 2 == 0

print(is_even(4))#True
print(is_even(7))#False

def is_even(n):
    return n % 2 == 0

def check_number(n):
    if is_even(n):
        return "偶数"
    else:
        return "奇数"

print(check_number(10))
print(check_number(7))

def is_even(n):
    return n % 2 == 0

def count_even(numbers):
    count = 0
    for n in numbers:
        if is_even(n):
            count += 1
    return count
print(count_even([1,2,3,4,6]))

