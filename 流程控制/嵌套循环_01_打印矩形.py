#打印 n 行 m 列的矩形
n = int(input("请输入行数:"))
m = int(input("请输入列数:"))
for i in range(n):
    for j in range(m):
        print("*",end=" ")#不换行的用法
    print()#换行的用法
