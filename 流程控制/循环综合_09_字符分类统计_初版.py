#练习7:
num1 = 0
num2 = 0
num3 = 0
num4 = 0
a = input("请输入一行字符:")
for i in a:
    for j in range(10):
        if i==str(j):
            num1+=1
    for k in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
        if i==k:
            num2+=1
    if i==" ":
        num3+=1
    else:
        num4+=1
print(f"数字数为:{num1}")
print(f"英文字母数为:{num2}")
print(f"空格数为:{num3}")
print(f"其他字符数为:{num4}")
