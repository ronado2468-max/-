def sum_positive(numbers):
    return sum(n for n in numbers if n > 0)
result = sum_positive([1,2,3,4,5])
print(result)

def has_positive(numbers):
    return any(n > 0 for n in numbers)
result = has_positive([1,-2,3,4,5])
print(result)

def all_positive(numbers):
    return all(n > 0 for n in numbers)
result = all_positive([1,-2,3,4,5])
print(result)

def max_positive(numbers):
    positive = [n for n in numbers if n > 0]

    if len(positive) == 0:
        return "NONE"
    else:
        return max(positive)
print(max_positive([3,-5,10,2]))