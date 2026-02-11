#買い物リスト管理プログラム

print("=== 買い物リストへようこそ! ===")

# 1. 空のリストを作る(ここに買い物アイテムを入れる)
shopping_list = []
prices = [] #値段も一緒に管理しよう

#2 アイテムを3～5個追加してみよう(自分で入力)

max_items = 5 #最大5個まで
count = 0

print(f"\n買い物を追加していこう!(最大{max_items}個まで)")

while count < max_items:
    item = input(f"商品名({count+1}/{max_items})(終了したいときは'終わり'):")
    if item == "終わり":
        break

    try:
        price = int(input(f"{item}の値段(円) :"))
    except:
        print("数字で入力してね!もう一度～")
        continue

    shopping_list.append(item)
    prices.append(price)
    print(f"→ {item}({price}円)を追加しました!")
    count += 1 #ここでカウントアップ
if count == max_items:
    print(f"\n{max_items}個に達しました!これ以上追加できません。")

#3 .リストの中身を表示
print("\n現在の買い物リスト:")
if len(shopping_list) == 0:
    print("まだ何も入ってないよ")
else:
    total = 0
    for i in range(len(shopping_list)):
        print(f"{i+1}.{shopping_list[i]} → {prices[i]}円")

        total += prices[i]

#4 ちょっとした判定
if total > 5000:
    print("今日は豪華な買い物だね")
elif total > 2000:
    print("いい感じの買い物だね")
else:
    print("今日は軽めの買い物")