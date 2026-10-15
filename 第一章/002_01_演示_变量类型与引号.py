#变量类型的判断
a = 4.02
print(type(a))
#(变量,类型)
print(isinstance(a, float))
print(isinstance(a, int))
print(isinstance(a, str))
b = 718
print(isinstance(b,bool))

#引号的用法
print("狼狈比失去难受")
print("""我怀念的是
                无话不说""")
#转义字符\' \" \n \t
print('It\'s a good day')
print("他很\"重要\"")
print("唧唧复唧唧\n木兰当户织")
print("\t同行十二年\n\t不知木兰是女郎")

#字符串的拼接
name = "帅哥"
age = 18
pro = "student"
hobby= "跑步"
print("大家好,我的名字是:"+name+",年龄:"+str(age)+",身份是:"+pro+",爱好是:"+hobby)
