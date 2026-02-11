
def sei_kazu(numbers):
    result = [n for n in numbers if n > 0]

    if not result:
        return "NONE"
    
    m = max(result)
    if m >= 100:
        status = "EXCELLENT"
    elif m >= 50:
        status = "GOOD"
    else:
        status = "OK"
    return{
        "max": m,
        "status": status
    }
#①最大値が50以上の時だけOK
def judge_over_ok(numbers):
    result = sei_kazu(numbers)

    if result == "NONE":
        return "NG"

    if result["max"] >= 50:
        return "OK以上"
    else:
        return "NG"
print(judge_over_ok([20,30,60]))

#②EXCELLENT→最高
def convert_status(numbers):
    result = sei_kazu(numbers)

    if result == "NONE":
        return None

    if result["status"] == "EXCELLENT":
        return "最高"
    elif result["status"] == "GOOD":
        return "良"
    else:
        return "可"
print(convert_status([40,50,60]))
    
#最終ジャッジ
def final_judge(numbers):
    base = judge_over_ok(numbers)
    status = convert_status(numbers)

    if status is None:
        return None
    
    return f"{base}:{status}"
print(final_judge([10,60,3]))