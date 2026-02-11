#正の数だけを対象にし最小値を返す
def min_positive(numbers):
    result = [n for n in numbers if n > 0]

    if len(result) == 0:
        return "NONE"
    else: 
        return min(result)
print(min_positive([2,3,4,5]))