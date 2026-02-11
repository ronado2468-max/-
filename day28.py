def sei_kazu(numbers):
    result = [n for n in numbers if n > 0]
    
    if not result:
        return "NONE"
    
    m = max(result)
    if m >= 100:
        statsu = "EXCELLENT"
    elif m >= 50:
        statsu = "GOOD"
    else:
        statsu = "OK"
    
    return{
        "max": m,
        "statsu": statsu
    }
print(sei_kazu([4,5,6]))



    



def sei_kazu(numbers):
    result = [n for n in numbers if n > 0]
    
    if not result:
        return "NONE"
    
    m = max(result)
    if m >= 100:
        statsu = "EXCELLENT"
    elif m >= 50:
        statsu = "GOOD"
    else:
        statsu = "OK"
    
    return{
        "max": m,
        "statsu": statsu
    }
data = sei_kazu([23,45,2])

if data == "NONE":
    print("正の数がありません")
else:
     print("最大値", data["max"])
     print("評価",data["statsu"])


def sei_kazu(numbers):
    result = [n for n in numbers if n > 0]
    
    if not result:
        return "NONE"
    
    m = max(result)
    if m >= 100:
        statsu = "EXCELLENT"
    elif m >= 50:
        statsu = "GOOD"
    else:
        statsu = "OK"
    
    return{
        "max": m,
        "statsu": statsu
    }

result = sei_kazu([23,45,120])

if result != "NONE" and result["statsu"] == "EXCELLENT":
        print("EXCELLENT")


def sei_kazu(numbers):
    result = [n for n in numbers if n > 0]
    
    if not result:
        return "NONE"
    
    m = max(result)
    if m >= 100:
        statsu = "EXCELLENT"
    elif m >= 50:
        statsu = "GOOD"
    else:
        statsu = "OK"
    
    return{
        "max": m,
        "statsu": statsu
    }

result = sei_kazu([10,60,3])

if result == "NONE":
    print("NO DATA")
else:
    if result["statsu"] == "EXCELLENT":
        print("最高評価:", result["max"])
    else:
        print("評価:", result["statsu"])

def sei_kazu(numbers):
    result = [n for n in numbers if n > 0]

    if not result:
        return "NONE"
    
    m = max(result)

    if m >= 100:
        statsu = "EXCELLENT"
    elif m >= 50:
        statsu = "GOOD"
    else:
        statsu = "OK"
    return statsu

result = sei_kazu([10,100,3])

if result == "NONE":
    print("NO DATA")
elif result == "EXCELLENT":
    print("EXCELLENT")


def sei_kazu(numbers):
    result = [n for n in numbers if n > 0]

    if not result:
        return "NONE"
    
    m = max(result)

    if m >= 100:
        statsu = "EXCELLENT"
    elif m >= 50:
        statsu = "GOOD"
    else:
        statsu = "OK"
    return {
        "max": m,
        "statsu": statsu
    }

result = sei_kazu([20,100,3])

if result != "NONE" and result["statsu"] == "EXCELLENT":
    print(f'EXCELLENT: 最大値は{result["max"]}')
