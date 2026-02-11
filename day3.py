age = 20

if age >= 18:
    print("大人です")
else:
    print("子供です")

score = 75

if score >= 90:
    print("Sランク")
elif score >= 70:
    print("Aランク")
else:
    print("Bランク")

name = "修"

if name == "修":
    print("一致")
else:
    print("違う")

age = int(input("あなたの年齢は?: "))

if age >= 18:
    print("大人です")
else:
    print("子供です")

score = int(input("点数を入力(0～100): "))

if score >= 90:
    print("Sランク")
elif score >= 70:
    print("Aランク")
elif score >= 50:
    print("Bランク")
else:
    print("Cランク")

password = input("パスワードを入力: ")

if password == "abc123":
    print("ログイン成功")
else:
    print("パスワードが違います")
