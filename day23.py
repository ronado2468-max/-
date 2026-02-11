def seikazu(numbers):
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)
    return result
print(seikazu([1,-2,3,0,5]))

def seikazu_a(numbers):
    result = seikazu(numbers)
    

    if len(result) >= 3:
        return "OK"
    else:
        return "NG"
print(seikazu_a([1,-2,3,0,5]))

def seikazu_b(numbers):
    result = seikazu_a(numbers)
    return result
print(seikazu_b([1,-2,3,0,5])) 



        
            