def gusu_number(number):
    
        if number % 2 == 0:
            return "even"
        else:
            return "odd"
result = gusu_number(9)
print(result)

def count_positive(number):
    count = 0
    for n in number:
         if n > 0:
              count += 1
    return count
result = count_positive([1,-2,3,0,5])
print(result)

def sum_positive(number):
    total = 0
    for n in number:
        if n > 0:
             total += n
    return total
result = sum_positive([1,-3,5,0,2])
print(result)

def avarage_positive(numbers):
    count = 0
    total = 0
    for n in numbers:
        if n > 0:
             count += 1
             total += n
         
    return total / count
result = avarage_positive([1,-2,3,0,6])
print(result)