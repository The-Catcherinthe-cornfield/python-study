# s = "Hello World 123"
# su = s.upper()
# print(su)
# sl = s.lower()
# print(sl)
# print("-------------------")
# #is判断
# print("abc123".isalnum())   # True，字母或数字
# print("123".isdigit())      # True，纯数字
# print("abc".isalpha())      # True，纯字母
# print("abc 123".isalnum())  # False，有空格

#练习4:
# text = "I like Python, and python is easy. I love Python."
# a = text.count('Python')
# print(a)
# b = text.count('python')
# print(a+b)
# c = text.find('Python')
# print(c)
# d = text.find('Java')
# print(d)
# print('Python'in text)          #用in来寻找左边是否在右边里面

#练习5:
# s = "   hello world   "
# print(s.strip())
# print(s.lstrip())     #左或者右的删除l/r
# print(s.rstrip())

#练习6:
# s = "苹果,香蕉,橙子"
# list = s.split(',')
# print(list)    #字符串直接转化成列表
# jions = "_".join(list)
# print(s.replace(',','_'))   #列表用join,字符串用replace
# print(jions)

#练习7:
# text = "I like apples and bananas."
# print(text.replace('a','*'))
# print(text.replace('a','*',1))    #第三个数可以限定替换几个
# print(text.replace('a','*',2))
# print(text)

#练习8:
# r1 = []
# r2 = []
# text = input("请输入一串字符:")
# for i in text[::]:
#     r1.append(i)
# print(r1)
# for j in text[::-1]:
#     r2.append(j)
# print(r2)
# if r1==r2:
#     print(f"{text}是回文数")

#***********简化版
# text = input()
# if text==text[::-1]:
#     print("是")
# else:
#     print("不是")
#
# #**********不区分大小写和空格版:
# text = input("请输入一串字符:").lower().replace(" ","")   #全部变成一样的大或小写即可
# if text==text[::-1]:
#     print("是")
# else:
#     print("不是")

#练习9 输出单词数:
# text = input("请输入一段英文:")
# print(len(text.strip(' ')))   #strip只能去除两端的符号
# print(text.split(' '))
# print(len(text.split(' ')))

# sentence = input("请输入一句英文：")
# words = sentence.split()        #数数量应该先拆分成列表用split
# # print(words)
# # print(words[0])
#
# abbr = ""
# for w in words:
#     abbr += w[::]
#
# print(f"单词数：{len(words)}")
# print(f"缩写：{len(abbr)}")

#练习10:
print("10" > "9")










