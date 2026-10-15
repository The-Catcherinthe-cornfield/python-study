#bmi计算
h = float(input("请输入身高: "))
w = float(input("请输入体重: "))
bmi = float(f"{w/(h*h):.2f}")
if bmi < 18.5:
    print("偏瘦")
    if bmi>=18.5 and bmi<=23.9:
        print("正常")
    elif bmi>=24 and bmi<=27.9:
        print("超重")
    elif bmi >=28:
        print("肥胖")
