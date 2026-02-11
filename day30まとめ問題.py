data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 90},
    {"name": "Dave", "score": 60},
    {"name": "Eve", "score": 88}
]

result = []

for item in data:
    if item["score"] >= 80:
        result.append({
        "name": item["name"],
        "score": item["score"]
        })

print(result)