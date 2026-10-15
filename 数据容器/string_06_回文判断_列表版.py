#练习8:
r1 = []
r2 = []
text = input("请输入一串字符:")
for i in text[::]:
    r1.append(i)
print(r1)
for j in text[::-1]:
    r2.append(j)
print(r2)
if r1==r2:
    print(f"{text}是回文数")
