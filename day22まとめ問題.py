#偶数を集めたリスト
def gusu_even(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
print(gusu_even([1,2,3,4,5]))

#正の数を集めたリスト
def sei_even(numbers):
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)
    return result
print(sei_even([-3,0,5,-1,8]))

#総合
def seikosu_even(numbers):
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)

    if len(result) >= 3:
        return "OK"
    else:
        return "NG"
print(seikosu_even([1,-1]))