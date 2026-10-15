#练习9 输出单词数:
text = input("请输入一段英文:")
print(len(text.strip(' ')))   #strip只能去除两端的符号
print(text.split(' '))
print(len(text.split(' ')))
