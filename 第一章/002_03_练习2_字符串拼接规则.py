#练习2:  字符串的拼接中+ 号两边要么都是字符串，要么都是数字，不能混着来!!!!!
name = input("请输入名字:")
age = input("请输入年龄:")
# print(name + "明年" + int(age)+int(1)+ "岁")错误示范
print(name + "明年" + str(int(age)+1)+ "岁")
