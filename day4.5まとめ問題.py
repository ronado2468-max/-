#追加して表示
animals = ["cat","dog"]
animals.append("bird")
print(animals)

#昇順に並び替える
numbers = [5,1,9,3]
numbers.sort()
print(numbers)

#年齢を表示(キーだけ)
prices = {
    "Aki":20,
    "Beni":25,
}
print(prices["Beni"])

#キーと値を表示
prices = {
    "cola":120,
    "tea":100,
}
for item, price in prices.items():
    print(item,price)

#自分で辞書作る

prices = {
    "Ronaldo":95,
    "Ronaldinho":94,
    "NeymarJr":93,
    "VinciusJr":85,
}

for item, price in prices.items():
    print(item,price)
    

