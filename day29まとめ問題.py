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
#１
def count_good_or_excellent(data_list):
    count = 0

    for numbers in data_list:
        result = sei_kazu(numbers)

        if result != "NONE":
            if result["status"] == "GOOD" or result["status"] == "EXCELLENT":
                count += 1

    return count

data = [
    [10,20,30],
    [50,2],
    [-3,-1],
    [120]
]

print(count_good_or_excellent(data))

#２
def convert_status_list(data_list):
    result_list = []

    for numbers in data_list:
        result = sei_kazu(numbers)

        if result != "NONE":
            if result["status"] == "EXCELLENT":
                result_list.append("最高")
            elif result["status"] == "GOOD":
                result_list.append("良")
            else:
                result_list.append("可")

    return result_list

data = [
    [10,20,30],
    [50,2],
    [-3,-1],
    [120]
]

print(convert_status_list(data))

#３
def extract_max_values(data_list):
    max_list = []

    for numbers in data_list:
        result = sei_kazu(numbers)

        if result != "NONE":
            if result["status"] == "EXCELLENT" or result["status"] == "GOOD":
                max_list.append(result["max"])

    return max_list

data = [
    [10,20,30],
    [50,2],
    [-3,-1],
    [120]
]

print(extract_max_values(data))