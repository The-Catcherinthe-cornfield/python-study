# #变量类型的判断
# a = 4.02
# print(type(a))
# #(变量,类型)
# print(isinstance(a, float))
# print(isinstance(a, int))
# print(isinstance(a, str))
# b = 718
# print(isinstance(b,bool))
#
# #引号的用法
# print("狼狈比失去难受")
# print("""我怀念的是
#                 无话不说""")
# #转义字符\' \" \n \t
# print('It\'s a good day')
# print("他很\"重要\"")
# print("唧唧复唧唧\n木兰当户织")
# print("\t同行十二年\n\t不知木兰是女郎")

# #字符串的拼接
# name = "帅哥"
# age = 18
# pro = "student"
# hobby= "跑步"
# print("大家好,我的名字是:"+name+",年龄:"+str(age)+",身份是:"+pro+",爱好是:"+hobby)

#***************************************************************************
#Codex数据类型与运算总结练习
#练习1:'f'的拼接
# name = "小明"
# age = 12
# print(f"我是{name},今年{str(age)}岁")

#练习2:  字符串的拼接中+ 号两边要么都是字符串，要么都是数字，不能混着来!!!!!
# name = input("请输入名字:")
# age = input("请输入年龄:")
# # print(name + "明年" + int(age)+int(1)+ "岁")错误示范
# print(name + "明年" + str(int(age)+1)+ "岁")

#练习3:时间转换
# pc = input("请输入一个秒数:")#键盘录入字符类型为字符串后面注意转换!
# h = int(pc)//3600
# m = int(pc)%3600//60
# s = int(pc)%3600%60
# print(f"现在是{h}时{m}分{s}秒")

#练习4:温度转换
# C = input("请输入摄氏温度:")
# F = float(C)*1.8+32
# print(f"{F:.1f}")#*****注意保留几位小数的写法!固定f"{变量:.几位f}"

#练习5:打折计算
# app = 5.5
# ban = 3
# pay = (app*2.5+ban*4)*0.8
# print(f"{pay:.2f}")

#练习6:判定偶数
# x = 18
# result = x%2
# print(result==0)

#练习7:
# x = 5
# print(x * 3)
# print(x + 3)

#练习8:
p = float(input("商品单价:"))
pcs = float(input("购买数量:"))
pay = float(input("实付金额:"))
re = pay-pcs*p
if pay>=pcs*p:
    print(f"应找回{re:.2f}")
else:print("买不起")







