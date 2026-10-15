#练习4:
text = "I like Python, and python is easy. I love Python."
a = text.count('Python')
print(a)
b = text.count('python')
print(a+b)
c = text.find('Python')
print(c)
d = text.find('Java')
print(d)
print('Python'in text)          #用in来寻找左边是否在右边里面
