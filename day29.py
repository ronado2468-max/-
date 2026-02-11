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

def collect_status(data_list):
    results = []

    for numbers in data_list:
        result = sei_kazu(numbers)

        if result == "NONE":
            results.append("NONE")
        else:
            results.append(result["status"])

    return results

data = [
    [10,20,30],
    [50,2],
    [-3,-1],
    [120]
]

print(collect_status(data))


def count_status(data_list):
    counts = {
        "EXCELLENT": 0,
        "GOOD": 0,
        "OK": 0,
        "NONE": 0
    }

    for numbers in data_list:
        result = sei_kazu(numbers)

        if result == "NONE":
            counts["NONE"] += 1
        else:
            counts[result["status"]] += 1
    
    return counts

data = [
    [10,20,30],
    [50,2],
    [-3,-1],
    [120]
]

print(count_status(data))

def filter_good_or_excellent(data_list):
    results = []

    for numbers in data_list:
        result = sei_kazu(numbers)

        if result == "NONE":
            continue

        if result["status"] == "GOOD" or result["status"] == "EXCELLENT":
            results.append(numbers)

    return results

data = [
    [10,20,30],
    [50,2],
    [-3,-1],
    [120]
]

print(filter_good_or_excellent(data))


