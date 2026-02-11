def check(n):
    if n > 0:
        return "positive"
    else:
        return "not positive"
check(3)
print((check)(3))

def check2(n):
    if n > 0:
        return "positive"
check2(-1)
print((check2)(-1))

def sign(n):
    if n > 0:
        return "positive"
    elif n == 0:
        return "zero"
    else:
        return "negative"
sign(0)
print(sign(0))

def judge(n):
    if n >= 10:
        return "big"
    else:
        return "small"
judge(10)
print(judge(10))

def level(score):
    if score > 80:
        return "A"
    elif score > 60:
        return "B"
    else:
        return "C"
level(80) 
print(level(80))