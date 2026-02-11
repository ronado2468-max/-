#0以上の数の平均を返す関数
def average_non_negative(numbers):
    total = 0
    count = 0
    for n in numbers:
        if n >= 0:
            total += n
            count += 1
    return total / count
result = average_non_negative([4,12,4,6,7])
print(result)

#0以上の数が1つもない場合　それ以外平均
def average_non_negative_safe(numbers):
    total = 0
    count = 0
    for n in numbers:
        if n >= 0:
            total += n
            count += 1
    if count == 0:
        return "NONE"
    else:
        return total / count
result = average_non_negative_safe([-3,-5,-6])
print(result)

#総合
def judge_positive_total(numbers):
    total = 0
    count = 0
    for n in numbers:
        if n > 0:
            total += n
            count += 1
    if total >= 50:
        return "BIG"
    elif total >= 1:
        return "SMALL"
    else:
        return "NONE"
result = judge_positive_total([3,4,5])
print(result)