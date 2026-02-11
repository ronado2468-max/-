def judge_numbers(numbers):
    result = [n for n in numbers if n > 0]

    if not result:
        return {"status": "NONE"}

    total = sum(result)

    if total >= 100:
        status = "EXCELLENT"
    elif total >= 50:
        status = "GOOD"
    else:
        statsu = "OK"

    return {
        "total": total,
        "status": status
    }

print(judge_numbers([3,4,40,6]))

def judge_numbers(numbers):
    result = [n for n in numbers if n > 0]

    if not result:
        return{"判定": "NONE"}
    
    m = max(result)

    if m >= 100:
        statsu = "EXCELLENT"
    elif m >= 50:
        statsu = "GOOD"
    else:
        statsu = "OK"

    return{
        "最大値": m,
        "判定": statsu
    }

print(judge_numbers([20,3,40]))

def judge_numbers(numbers):
    result = [n for n in numbers if n > 0]

    if not result:
        return{"判定": "NONE"}
    
    m = max(result)

    if m >= 100:
        statsu = "EXCELLENT"
    elif m >= 50:
        statsu = "GOOD"
    else:
        statsu = "OK"

    return{
        "最大値": m,
        "判定": statsu
    }

print(judge_numbers([20,3,40]))