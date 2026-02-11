data = [
    {"name": "A", "score": 92},
    {"name": "B", "score": 45},
    {"name": "C", "score": 77},
    {"name": "D", "score": 88},
]

def judge(score):
    if score >= 80:
        return "EXCELLENT"
    elif score >= 50:
        return "GOOD"
    else:
        return "FAIL"

for item in data:
    if judge(item["score"]) == "EXCELLENT":
        print(item["name"])



data = [
    {"name": "A", "score": 92},
    {"name": "B", "score": 45},
    {"name": "C", "score": 77},
    {"name": "D", "score": 88},
    {"name": "E", "score": 50},
]

def judge(score):
    if score >= 80:
        return "EXCELLENT"
    elif score >= 50:
        return "GOOD"
    else:
        return "FAIL"

result = {}

for item in data:
    status = judge(item["score"])
    if status in result:
        result[status] += 1
    else:
        result[status] = 1
print(result)


data = [
    {"name": "A", "score": 92},
    {"name": "B", "score": 45},
    {"name": "C", "score": 77},
    {"name": "D", "score": 88},
    {"name": "E", "score": 50},
]

def judge(score):
    if score >= 80:
        return "EXCELLENT"
    elif score >= 50:
        return "GOOD"
    else:
        return "FAIL"

excellent_name = []

for item in data:
    status = judge(item["score"])
    if status == "GOOD":
        excellent_name.append(item["name"])

print(excellent_name)


data = [
    {"name": "A", "score": 92},
    {"name": "B", "score": 45},
    {"name": "C", "score": 77},
    {"name": "D", "score": 88},
    {"name": "E", "score": 50},
]

def judge(score):
    if score >= 80:
        return "EXCELLENT"
    elif score >= 50:
        return "GOOD"
    else:
        return "FAIL"
    
result = {}

for item in data:
    status = judge(item["score"])
    if status != "FAIL":
        result[item["name"]] = judge(item["score"])

print(result)