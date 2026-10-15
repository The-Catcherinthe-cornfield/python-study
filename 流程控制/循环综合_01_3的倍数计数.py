#练习1:
a = 0
i = 1
n = int(input("请输入一个正整数:"))
while i<=n:
    if i%3==0 and i%5!=0:
        print(i ,end=" ")
        a+=1
    i+=1
print(f"正整数个数为{a}")
