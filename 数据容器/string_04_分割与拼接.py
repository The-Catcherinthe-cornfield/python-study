#练习6:
s = "苹果,香蕉,橙子"
list = s.split(',')
print(list)    #字符串直接转化成列表
jions = "_".join(list)
print(s.replace(',','_'))   #列表用join,字符串用replace
print(jions)
