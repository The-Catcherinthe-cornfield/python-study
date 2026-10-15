#分数与等级
score = float(input("请输入你的分数:"))
if score>=0 and score<=100:
    if score>=90:
        print("等级为:A")
    elif score>=80 and score<=89:
        print("等级为:B")
    elif score >= 70 and score <= 79:
        print("等级为:C")
    elif score >= 60 and score <= 69:
        print("等级为:D")
    elif score < 60:
        print("等级为:E")
else:
    print("成绩不合法")
