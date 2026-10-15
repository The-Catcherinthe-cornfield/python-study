#************更好的表达
h = float(input("请输入身高: "))
w = float(input("请输入体重: "))
bmi =float (f"{w/(h*h):.2f}")#注意运算顺序乘除是等价的所以要用括号
if bmi < 18.5:
    print("偏瘦")
elif bmi< 24:
        print("正常")
elif bmi< 28:
        print("超重")
else :
        print("肥胖")#从低到高排序这样写可以让程序自动分层
