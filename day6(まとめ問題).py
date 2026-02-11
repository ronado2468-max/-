def is_big(numbers):
    s = 0
    for n in numbers:
        s += n
    

    if s >=10:
        return True
    else:
        return False
    
print(is_big([1,2,3,4]))


    

