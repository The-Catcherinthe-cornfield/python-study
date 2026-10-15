#练习三角形类型判断:
a = int(input("请输入第1条边"))
b = int(input("请输入第2条边"))
c = int(input("请输入第3条边"))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("三角形为等边三角形")
    elif a==b or b==c or a==c:
        print("三角形为等腰三角形")
    else:
        print("三角形为普通三角形")
else:
        print("三角形不存在")
