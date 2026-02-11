# Day5: Excelファイルをpandasで読み込む!

print("=== Day 5: Excel読み込みスタート! ===")

import pandas as pd #これが大事!pandasを使う宣言

# 1. Excelファイルを読み込む(一番基本)
file_name = "test_new.xlsx" #ここを新しいファイル名に変えたよ

df = pd.read_excel(r"C:\Users\PC\PythonProjects\MyProject\grop\test_new.xlsx") # これで一行でExcelがDataFrameになる!

# 2. 読み込んだデータを表示
print("\nExcelの内容全部を表示:")
print(df) #表全体が出る

print("\n最初の5行だけ(head()):")
print(df.head()) #デフォルトで上5行

print("\n列名だけ見てみる:")
print(df.columns) #商品 単価 数量みたいなのがでる

print("\n合計金額を計算してみる(自分で追加!)")
df["合計金額"] = df["単価"] * df["数量"] #新しい列を作る!
print(df)

#おまけ:簡単な集計
print("\n合計金額の合計:", df["合計金額"].sum(),"円")