#练习1:
# for i in range(2 ,101, 2):
#     print(i)

练习2:
for i in range(10 , 0, -1):#步长为负数就是倒着走
    print(i)

#练习2:
# sum = 0
# for i in range(1, 101):
#     sum+= i
# print(sum)

#练习3:
# f = 1
# for i in range(1 , 6):
#     f *= i
# print(f)

练习4:
i = 0
s = "helloworld"
for c in s:
    if c == "o":
        i+=1
print(i)

#练习5:(for else)
n = int(input("请输入一个大于1的整数:"))
for i in range(2,n):
    if(n%i==0):
        print(f"{n}可以被{i}整除")
        break#break在这里打断的是for else一个整体else也不会执行
else:#for只要没有break就会执行即使在这里n是一个质数if一次都没过
    print(f"{n}是一个质数")






































