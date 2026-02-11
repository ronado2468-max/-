def double(n):
    result = n * 2
    return result

x = double(5)
print(x)

def show_double(n):
    print(n * 2)

y = show_double(5)
print(y)

def add(a,b):
    print(a+b)

result = add(3,4)
print(result + 1)

#使いにくい関数
def add(a,d):
    print(a+b)

    x= add(3,4)
    print(x+1)


#使える関数
def add(a,b):
    return a + b

    x = add(3,4)
    print(x+1)

def triple(n):
    return n * 3

print(triple(4))