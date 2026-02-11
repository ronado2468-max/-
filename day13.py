def add(a,b):
    return a + b

result = add(3,5)
print(result)

def double(n):
    return n * 2

x = double(4)
print(x)

def count_even(a):
    count = 0
    for n in a:
        if n % 2 == 0:
            count += 1
    return count
result = count_even([1,2,3,4,5])
print(result)

def sum_over_10(sum):
    total = 0
    for n in sum:
        if n >= 10:
           total += n
    return total
result = sum_over_10([3,10,5,20])
print(result)

def pick_long_words(a):
    result = []
    for word in a:
        len(word)
        if len(word) >= 3:
            result.append(word)
    return result
result = pick_long_words(["a","cat","dog","hi","pen"])
print(result)

def sum_even(sum):
    total = 0
    for n in sum:
        if n % 2 == 0:
            total += n
    return total
result = sum_even([1,2,3,4,5])
print(result)



    

    