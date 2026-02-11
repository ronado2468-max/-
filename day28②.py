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

    return {
        "max": m,
        "status": status
    }

result = sei_kazu([23,45,2])

if result != "NONE":
    if result["status"] == "GOOD":
        print("GOOD")
    elif result["status"] == "OK":
        print("OK")