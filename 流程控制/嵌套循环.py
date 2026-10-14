# n = int(input("请输入行数:"))
# m = int(input("请输入列数:"))
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")#不换行的用法
#     print()#换行的用法

#练习2:
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()

#练习3:
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#练习4:
# n = int(input("请输入行数:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(0,2*i-1):
#         print("*",end="")#并列循环
#     print()

#练习5:空心图形"or"的用法:只负责打有符号的位置即可
# n = 5
# for i in range(n):#i表示行
#     for j in range(n):#j表示列固定的
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#练习6:
# n = 5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#练习7:
# for n in range(2,101):
#     is_prime = True    #运用标志变量
#     for i in range(2,n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n,end=" ")

#练习8:
for i in range(1,10):
    for j in range(i,10):
        if i+j == 10:
            print(i,j)
















