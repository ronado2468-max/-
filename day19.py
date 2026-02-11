def sum_even(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total


def double_even_sum(numbers):
    total = sum_even(numbers)
    return total * 2
result = double_even_sum([1,2,3,4,6])
print(result)

def positive_sum(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total


def judge_positive_sum(numbers):
    total = positive_sum(numbers)
    if total >= 20:
        return "BIG"
    else:
        return "SMALL"
result = judge_positive_sum([1,-3,10,15,-2])
print(result)
