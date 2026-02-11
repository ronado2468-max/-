#正の数の合計を返す関数
def sum_even(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total
#合計が30以上ならOK,未満ならNG
def dog_sum_even(numbers):
    total = sum_even(numbers)
    if total >= 30:
        return "OK"
    else:
        return "NG"
result = dog_sum_even([2,50,-9,-3,4])
print(result)
#正の数が一つもない場合は"NONE"それ以外の場合"正の数の合計を返す"
def pit_sum_even(numbers):
    count = 0
    total = 0
    for n in numbers:
        if n > 0:
           count += 1
           total += n
    if count == 0:
       return "NONE"
    else:
       return total
result = pit_sum_even([0,-44,-1])
print(result)

