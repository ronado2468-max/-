import pandas as pd

#エクスプローラーで右クリック [パスをコピー]してここに貼り付け
file_path = r"C:\Users\PC\PythonProjects\MyProject\grop\test_sales.xlsx"

df = pd.read_excel(file_path)
print(df.head())
