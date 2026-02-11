def square(n):
    return n * n

print(square(5))
print(square(2))

def calc(n):
    return n + 5

a = calc(3)
b = calc(a)

print(calc(3))
print(calc(a))