#偶数の合計を返す関数
def is_even(n):
    return n % 2 == 0

def sum_even(numbers):
    total = 0
    for n in numbers:
        if is_even(n):
           total += n
    return total

print(sum_even([1,2,3,4,6]))#12
