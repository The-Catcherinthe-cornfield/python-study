#练习5:空心图形"or"的用法:只负责打有符号的位置即可
n = 5
for i in range(n):#i表示行
    for j in range(n):#j表示列固定的
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
