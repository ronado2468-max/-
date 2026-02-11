def sum_positive(numbers):
    return sum (n for n in numbers if n > 0)
print(sum_positive([1,2,3,4,5]))

def count_positive(numbers):
    return sum(1 for n in numbers if n > 0)
print(count_positive([1,2,3,4,5]))

def judge_sum(numbers):
    result =  sum ( n for n in numbers if n > 0)

    if result >= 50:
        return "BIG"
    elif result >= 1:
        return "SMALL"
    else:
        return "NONE"
print(judge_sum([1,2,3,4,5]))

def sum_positive(numbers):
    return sum(n for n in numbers if n > 0)

def judge_total(total):
    if total >= 50:
        return "BIG"
    elif total >= 1:
        return "SMALL"
    else:
        return "NONE"
def judge_numbers(numbers):
    total = sum_positive(numbers)
    return judge_total(total)
print(judge_numbers([2,3,4,5,60]))

def sum_positive(numbers):
    return sum(n for n in numbers if n > 0)

def judge_total(total):
    if total >= 100:
        return "HUGE"
    elif total >= 50:
        return "BIG"
    elif total >= 1:
        return "SMALL"
    else:
        return "NONE"

def judge_numbers(numbers):
    total = sum_positive(numbers)
    return judge_total(total)
print(judge_numbers([12,50]))


    