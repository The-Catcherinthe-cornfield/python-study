# *******改错:遍历输入用循环,条件判断用条件把所有可能列进if中
text = input("请输入一行字符:")

letters = 0
digits = 0
spaces = 0
others = 0

for ch in text:
    if "a" <= ch <= "z" or "A" <= ch <= "Z":    #考虑大小写（原来这句漏了冒号，拆分时补上了）
        letters += 1
    elif "0" <= ch <= "9":
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        others += 1

print(f"英文字母数为:{letters}")
print(f"数字数为:{digits}")
print(f"空格数为:{spaces}")
print(f"其他字符数为:{others}")
