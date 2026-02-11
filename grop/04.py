# Day 4: 買い物リストをファイルに保存＆読み込み

print("=== Day 4: ファイルを扱ってみよう! ===")

#前回のリストをここで再現(テスト用に最初にデータを入れておく)
shopping_list = ["牛乳", "卵","パン"]
prices = [200, 300, 150]

# 1. リストをテキストファイルに保存する
filename = "shopping_list.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write("買い物リスト\n")
    file.write("==============\n")

    total = 0
    for i in range(len(shopping_list)):
        line = f"{shopping_list[i]}:{prices[i]}円\n"
        file.write(line)
        total += prices[i]

        file.write("---------------------\n")
        file.write(f"合計: {total}円\n")

print(f"リストを{filename}に保存しました!")
print("フォルダ内を見てみてね(テキストファイルが出来てるはず)")

# 2. 保存したファイルを読み込んで表示
print("\n今度は保存したファイルを読み込んで表示します")

with open(filename, "r", encoding="utf-8") as file:
    content = file.read() #全部読み込む
    print(content)

print("おつかれさま!ファイルの読み書きできたね!")
print("これができれば,Excelの代わりにテキストで結果を残せるようになるよ")
