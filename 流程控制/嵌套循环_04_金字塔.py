#练习4:
n = int(input("请输入行数:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(0,2*i-1):
        print("*",end="")#并列循环
    print()
