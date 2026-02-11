#数値のリストを受け取り10以上の数を表す関数
def num(numbers):
    for n in numbers:
        if n >= 10:
            print(n)
num([10,2,3,5,69])

#数値のリストを受け取り偶数が何個あるか表す関数
def gusu(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return (count)
result = gusu([1,2,3,4,5])
print(result)

#数値のリスト受け取り最大値を返す関数を書く
def find_max(numbers):
    max_value =numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value
result =  find_max([4,8,50,30,10])
print(result)


    


