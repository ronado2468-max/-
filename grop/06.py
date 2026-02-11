# Day 6: Excel読み込み + 加工して出力保存

print("=== Day 6 加工して新しいExcelに出力します! ===")

import pandas as pd

file_name = "test_new.xlsx" #自分のファイル名に合わせる

df = pd.read_excel(r"C:\Users\PC\PythonProjects\MyProject\grop\test_new.xlsx") # これで一行でExcelがDataFrameになる!

print("\n元の表:")
print(df)

#合計金額列を追加
df["合計金額"] = df["単価"] * df["数量"]

print("\n合計金額列を追加した表:")
print(df)

#ここから出力保存(これが今日のメイン!)
output_file =\集計結果.xlsx" #出力ファイル名(好きな名前に変えてもOK)

df.to_excel(output_file, index=False) #index=Falseで余計な行番号を消す

print(f"\n保存完了!")
print(f"新しいファイル「{output_file}」が同じフォルダにできました")
print("エクスプローラーで開いてみてね!")
