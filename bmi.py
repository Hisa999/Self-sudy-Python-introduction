weight = input("体重をKg単位で入力してください")
height = input("身長をm単位で入力してください")
bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
    print("痩せてる")
elif bmi < 25:
    print("ふつう")
elif bmi < 35:
    print("ちょっと太ってる")
else:
    print("だいぶ太ってる")
