#练习三角形类型判断:
# a = int(input("请输入第1条边"))
# b = int(input("请输入第2条边"))
# c = int(input("请输入第3条边"))
# if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print("三角形为等边三角形")
#     elif a==b or b==c or a==c:
#         print("三角形为等腰三角形")
#     else:
#         print("三角形为普通三角形")
# else:
#         print("三角形不存在")

#判断奇偶数
# x = int(input("请输入一个整数"))
# if x%2==0:
#     print(f"{x}是偶数")
# else:
#     print(f"{x}是奇数")

#判断闰年
# year = int(input("请输入年份:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")

#分数与等级
# score = float(input("请输入你的分数:"))
# if score>=0 and score<=100:
#     if score>=90:
#         print("等级为:A")
#     elif score>=80 and score<=89:
#         print("等级为:B")
#     elif score >= 70 and score <= 79:
#         print("等级为:C")
#     elif score >= 60 and score <= 69:
#         print("等级为:D")
#     elif score < 60:
#         print("等级为:E")
# else:
#     print("成绩不合法")

#bmi计算
# h = float(input("请输入身高: "))
# w = float(input("请输入体重: "))
# bmi = float(f"{w/(h*h):.2f}")
# if bmi < 18.5:
#     print("偏瘦")
#     if bmi>=18.5 and bmi<=23.9:
#         print("正常")
#     elif bmi>=24 and bmi<=27.9:
#         print("超重")
#     elif bmi >=28:
#         print("肥胖")
#************更好的表达
# h = float(input("请输入身高: "))
# w = float(input("请输入体重: "))
# bmi =float (f"{w/(h*h):.2f}")#注意运算顺序乘除是等价的所以要用括号
# if bmi < 18.5:
#     print("偏瘦")
# elif bmi< 24:
#         print("正常")
# elif bmi< 28:
#         print("超重")
# else :
#         print("肥胖")#从低到高排序这样写可以让程序自动分层



#match的应用1:(相当于swith)
# day = int(input("请输入星期几:"))
# match day:
#     case 1:
#         print("星期一")
#     case 2:
#         print("星期二")
#     case 3:
#         print("星期三")
#     case 4:
#         print("星期四")
#     case 5:
#         print("星期五")
#     case 6:
#         print("星期六")
#     case 7:
#         print("星期七")
#     case _:
#          print("输入错误")

#应用2:
# a = float(input("请输入第一个数字:"))
# op = input("请输入运算符")
# b = float(input("请输入第二个数字:"))
# match op:
#     case '+':
#         print(f"运算结果为:{a+b:.2f}")
#     case '-':
#         print(f"运算结果为:{a-b:.2f}")
#     case '*':
#         print(f"运算结果为:{a*b:.2f}")
#     case '/':
#         if b!=0:
#             print(f"运算结果为:{a/b:.2f}")
#         else:
#             print("除数不能等于零")
#     case _:
#         print("运算符错误")

#改错:在case中运用条件判断:case x if x...
# score = 1
# match score:
#      case s if s>90:
#          print("优秀")
#      case s if s>60:
#           print("及格")
#      case _:
#          print("不及格")

#密码应用:
# i = 3
# s = "python123"
# while(i>=0):
#     a = input("请输入登录密码:")
#     if(a!=s):
#         print(f"密码错误,你还有{i}次登陆机会")
#         i-=1
#     else:
#         print("登录成功")
# print("账号已锁定")
































