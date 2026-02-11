def sei_kazu(numbers):
    result = [n for n in numbers if n > 0]

    if not result:
        return "NONE"
    
    m = min(result)

    if m >= 10:
        return "HIGH"
    else:
        return "LOW"


print(sei_kazu([12]))

def sei_total(numbers):
    result = [n for n in numbers if n > 0]
    
    if not result:
        return "NONE"
    
    m = sum(result)

    if m >= 100:
        return "BIG"
    else:
        return "SMALL"

print(sei_total([2,3,4,5]))