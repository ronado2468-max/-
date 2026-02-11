def add(a,b):
    return a + b
x = add(3,5)
print(x)

def show_sum(a,b):
    print (a + b)
def get_sum(a,b):
    return a + b

r1 = show_sum(2,3)
r2 = get_sum(2,3)

print(r1)
print(r2)

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(is_even(10))
print(is_even(7))

def total(numbers):
    s = 0
    for n in numbers:
        s += n
    return s
print(total([1,2,3,4]))

