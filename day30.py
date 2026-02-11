data = [
    {"name": "Alice","score": 85},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 90},
    {"name": "Dave", "score": 60}
]

for item in data:
    if item["score"] >= 80:
        print(item["name"])



data = [
    {"name": "Alice","score": 85},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 90},
    {"name": "Dave", "score": 60}
]

result = []

for item in data:
    if item["score"] >= 80:
        result.append(item["name"])


print(result)