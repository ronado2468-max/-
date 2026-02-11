#正の数だけを集める関数
def seikazu(numbers):
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)
    return result
print(seikazu([1,2,3,-2,-8]))

#合計で判定する関数
def seikazu_a(numbers):
    result = seikazu(numbers)
    if sum(result) >= 30:
        return "PASS"
    elif sum(result) >= 1:
        return "RETRY"
    else:
        return "FAIL"
print(seikazu_a([3,4,5,6]))

#まとめ役の関数
def seikazu_b(numbers):
    result = seikazu_a(numbers)
    return result
print(seikazu_b([8,80,7]))