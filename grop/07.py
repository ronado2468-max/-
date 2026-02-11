# Day 7: 複数Excelファイルをまとめて集計

print("=== Day 7: 複数ファイルをまとめて処理します! ===")

import pandas as pd
import glob # ファイル一覧を取るためのライブラリ

# 1. 対象のExcelファイルを全部探す(同じフォルダ内の .xlsx 全部)
# excel_files = glob.glob(r"C:\Users\PC\PythonProjects\MyProject\grop\*.xlsx") # *.xlsxで全部のExcelを探す

# もし特定のファイルだけならこう
excel_files = glob.glob(r"C:\Users\PC\PythonProjects\MyProject\grop\*sales_*.xlsx") # salesで始まるファイルだけ

print(f"見つかったファイル数: {len(excel_files)}")
print("ファイル一覧:")
for f in excel_files:
    print(" - " + f)

# 2. 全部のデータを入れる空のリスト
all_dfs = []

# 3. 1つずつ読み込んでリストに追加
for file in excel_files:
    print(f"\n処理中: {file}")
    try:
        df = pd.read_excel(file)
        all_dfs.append(df)
    except Exception as e:
        print(f"エラー(スキップ): {file} → {e}")

# 4. 全部をひとつにまとめる
if all_dfs:
    combined_df = pd.concat(all_dfs, ignore_index=True)

    print("\nまとめた表(最初の5行):")
    print(combined_df.head())

    # 合計金額列を追加
    combined_df["合計金額"] = combined_df["単価"] * combined_df["数量"]

    print("\n合計金額追加後(最初の5行):")
    print(combined_df.head())

    # 全体合計
    total_sum = combined_df["合計金額"].sum()
    print(f"\n全ファイルの合計金額: {total_sum} 円")

    # 出力保存
    output_file =  r"C:\Users\PC\PythonProjects\MyProject\grop\複数ファイル集計金額.xlsx"
    combined_df.to_excel(output_file, index=False)
    print(f"\n保存完了! → {output_file}")
    print("エクスプローラーで聞いて確認してね!")
else:
    print("読み込めるExcelファイルがありませんでした。")