fruits = ["apple","banana"]
fruits.append("orange")
print(fruits)

fruits = ["apple","banana","orange"]
fruits.remove("banana")
print(fruits)

numbers = [5,3,9,1]
numbers.sort()
print(numbers) #[1,3,5,9]

prices = {
    "apple": 120,
    "banana":80,
    "orange":100
}

print(prices["banana"]) #80

items = []
items.append("milk")
items.append("bread")
items.append("egg")

items.remove("bread")

print(items)

prices = {
    "apple": 120,
    "banana": 80,
    "orange": 100
}

item = input("商品名を入力: ")

if item in prices:
    print(prices[item], "円です")
else:
    print("その商品はありません")
