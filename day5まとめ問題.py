#Helloという関数
def hello():
    print("Hello")

hello()

#こんにちは、○○
def greet(name):
    print("こんにちは", name)

greet("Neymar")

#合計を出す
def add(a,b):
    return a + b

result = add(4,5)
print(result)

#リストの合計値
def total_price(prices):
      total = 0
      for price in prices:
        total += price
      return total
print(total_price([100,200,300])) #600

#偶数か奇数か
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(10)) #True
print(is_even(7)) #False


