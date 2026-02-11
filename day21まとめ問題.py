#合計
def sum_even(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total
#判定
def a_sum_even(total):
    if total >= 60:
        return "PASS"
    elif total >= 1:
        return "RETRY"
    else:
        return "FAIL"
#結果
def b_sum_even(numbers):
    total = sum_even(numbers)
    return a_sum_even(total)
result = b_sum_even([2,3,4,5,6])
print(result)
