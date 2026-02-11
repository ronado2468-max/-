from calendar import c


def hello():
    print("こんにちは")
    
hello()

def add(a , b):
    return a + b

result = add(3,5)
print(result) #8

def greet(name):
    print("こんにちは", name)

greet("Taro")    

def calc_average(a, b, c):
    total = a + b + c
    return total / 3

avg = calc_average(80, 70, 60)
print(avg)
