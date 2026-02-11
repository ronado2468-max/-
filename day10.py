def fee(age):
    if age < 12:
        return 0
    elif age < 65:
        return 500
    else:
        return 300
    
print(fee(65))

def discount(price):
    if price >= 1000:
        return price * 0.9
    elif price >= 500:
        return price * 0.95
    else:
        return price
print(discount(1000))

def discount2(price):
    if price >= 500:
        return price * 0.95
    elif price >= 1000:
        return price * 0.9
    else:
        return price
print(discount2(1000))
